import { DynamoDBClient, ScanCommand } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocument } from '@aws-sdk/lib-dynamodb';

const db = new DynamoDBClient({ region: 'us-east-1' });

const TABLE_NAME = 'ethomas-p2-dev'; 

const findAllMovies = async () => {
    const params = {
        TableName: TABLE_NAME
    };
    try {
        const command = new ScanCommand(params);
        const { Items: movies } = await db.send(command);
        return movies;
    } catch (error) {
        console.error('Error fetching movies:', error);
        throw error; // Rethrow the error to be caught by the caller
    }
};

const handler = async () => {
    try {
        const movies = await findAllMovies();
        const response = {
            statusCode: 200,
            headers: {
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*"
            },
            body: JSON.stringify(movies),
        };
        return response;
    } catch (error) {
        console.error('Error in Lambda execution:', error);
        return {
            statusCode: 500,
            body: JSON.stringify({ message: 'Internal Server Error' }),
        };
    }
};

export { handler }; 