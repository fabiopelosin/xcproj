#import "PBXTarget.h"
#import "XCConfigurationList.h"

@class NSPathStore2;

@protocol PBXProject <PBXContainer, NSObject>

+ (BOOL) isProjectWrapperExtension:(NSString *)extension;
+ (id<PBXProject>) projectWithFile:(NSString *)projectAbsolutePath;

- (NSArray *) targets; // PBXTarget
- (id<PBXTarget>) targetNamed:(NSString *)targetName;

- (NSString *) name;
- (NSPathStore2 *) path;

- (id<XCConfigurationList>) buildConfigurationList;

- (NSString *) expandedValueForString:(NSString *)string forBuildParameters:(id)buildParameters;

- (BOOL) writeToFileSystemProjectFile:(BOOL)projectWrite userFile:(BOOL)userWrite checkNeedsRevert:(BOOL)checkNeedsRevert;

@end
