import boto3

def create_cloudfront_distribution(s3_origin_domain):
    cloudfront_client = boto3.client('cloudfront')

    distribution_config = {
        'CallerReference': 'ethomas-p2',
        'Comment': 'CloudFront Distribution for ethomas-p2 project',
        'Enabled': True,
        'Origins': {
            'Quantity': 1,
            'Items': [{
                'Id': 'ethomas-p2-S3Origin',
                'DomainName': s3_origin_domain,
                'S3OriginConfig': {'OriginAccessIdentity': ''}
            }]
        },
        'DefaultCacheBehavior': {
            'TargetOriginId': 'ethomas-p2-S3Origin',
            'ViewerProtocolPolicy': 'https-only',
            'AllowedMethods': {
                'Quantity': 3,
                'Items': ['GET', 'HEAD', 'OPTIONS'],
                'CachedMethods': {
                    'Quantity': 2,
                    'Items': ['GET', 'HEAD']
                }
            },
            'Compress': True,
            'ForwardedValues': {'QueryString': False, 'Cookies': {'Forward': 'none'}},
            'MinTTL': 0,
            'DefaultTTL': 86400,
            'MaxTTL': 31536000,
        },
        'ViewerCertificate': {
            'CloudFrontDefaultCertificate': True,
            'MinimumProtocolVersion': 'TLSv1.2_2019'
        }
    }

    try:
        response = cloudfront_client.create_distribution(DistributionConfig=distribution_config)
        return response['Distribution']
    except boto3.exceptions.Boto3Error:
        return None

distribution = create_cloudfront_distribution('ethomas-p2.s3.amazonaws.com')


