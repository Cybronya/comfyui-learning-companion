---
key: 视频生成/图生视频/多角色替换Wan+Animate+OneToAll+Same3+SeedVR2.5_2000558063344025601.json
name: 多角色替换Wan+Animate+OneToAll+Same3+SeedVR2.5_2000558063344025601.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多角色替换Wan+Animate+OneToAll+Same3+SeedVR2.5_2000558063344025601.json
hash: addd4ae16e157736
coverage: 0.779412
learned_at: 2026-10-15 22:33:41
nodes: [GetVideoComponents, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, workflow>WanAnimate KJ加载器, SimpleMath+, WanVideoAnimateEmbeds, GetVideoComponents, workflow>角色图加序号, WanVideoAnimateEmbeds, GetVideoComponents, workflow>角色图加序号, PreviewImage, workflow>wanAnimate 采样, workflow>wanAnimate 采样, SaveVideoRGBA, PreviewImage, workflow>背景与主体遮罩, workflow>背景与主体遮罩, workflow>获取对象遮罩, GetImagesFromBatchIndexed, workflow>图像拼合, GetImagesFromBatchIndexed, workflow>图像拼合, workflow>图像拼合, workflow>获取对象遮罩, workflow>背景与主体遮罩, workflow>获取对象遮罩, Int, Int, workflow>角色图加序号, easy int, WanVideoAnimateEmbeds, workflow>wanAnimate 采样, SaveImage, Reroute, Reroute, Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), SaveVideoRGBA, workflow>面部与姿势检测, Any Switch (rgthree), PoseDetectionOneToAllAnimation, workflow>面部与姿势检测, Any Switch (rgthree), workflow>面部与姿势检测, Any Switch (rgthree), GetImagesFromBatchIndexed, LoadVideoWithFilename, LoadVideoWithFilename, PreviewImage, PoseDetectionOneToAllAnimation, PoseDetectionOneToAllAnimation, Fast Groups Muter (rgthree), LoadVideoWithFilename, easy framesEditor, LoadImage, LoadImage, Note, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization, VHS_LoadVideo, SaveVideoRGBA, SaveVideoRGBA, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/多角色替换Wan+Animate+OneToAll+Same3+SeedVR2.5_2000558063344025601.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000558063344025601.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（68 个）：
- `GetVideoComponents`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `workflow>WanAnimate KJ加载器`
- `SimpleMath+`
- `WanVideoAnimateEmbeds`
- `GetVideoComponents`
- `workflow>角色图加序号`
- `WanVideoAnimateEmbeds`
- `GetVideoComponents`
- `workflow>角色图加序号`
- `PreviewImage`
- `workflow>wanAnimate 采样`
- `workflow>wanAnimate 采样`
- `SaveVideoRGBA`
- `PreviewImage`
- `workflow>背景与主体遮罩`
- `workflow>背景与主体遮罩`
- `workflow>获取对象遮罩`
- `GetImagesFromBatchIndexed`
- `workflow>图像拼合`
- `GetImagesFromBatchIndexed`
- `workflow>图像拼合`
- `workflow>图像拼合`
- `workflow>获取对象遮罩`
- `workflow>背景与主体遮罩`
- `workflow>获取对象遮罩`
- `Int`
- `Int`
- `workflow>角色图加序号`
- `easy int`
- `WanVideoAnimateEmbeds`
- `workflow>wanAnimate 采样`
- `SaveImage`
- `Reroute`
- `Reroute`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `SaveVideoRGBA`
- `workflow>面部与姿势检测`
- `Any Switch (rgthree)`
- `PoseDetectionOneToAllAnimation`
- `workflow>面部与姿势检测`
- `Any Switch (rgthree)`
- `workflow>面部与姿势检测`
- `Any Switch (rgthree)`
- `GetImagesFromBatchIndexed`
- `LoadVideoWithFilename`
- `LoadVideoWithFilename`
- `PreviewImage`
- `PoseDetectionOneToAllAnimation`
- `PoseDetectionOneToAllAnimation`
- `Fast Groups Muter (rgthree)`
- `LoadVideoWithFilename`
- `easy framesEditor`
- `LoadImage`
- `LoadImage`
- `Note`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`
- `VHS_LoadVideo`
- `SaveVideoRGBA`
- `SaveVideoRGBA`
- `LoadImage`

## 知识

覆盖率 **78%**（53/68）

**有卡**：`GetVideoComponents`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`workflow>WanAnimate KJ加载器`、`SimpleMath+`、`WanVideoAnimateEmbeds`、`workflow>角色图加序号`、`workflow>wanAnimate 采样`、`SaveVideoRGBA`、`workflow>背景与主体遮罩`、`workflow>获取对象遮罩`、`GetImagesFromBatchIndexed`、`workflow>图像拼合`、`Int`、`easy int`、`SaveImage`、`workflow>面部与姿势检测`、`PoseDetectionOneToAllAnimation`、`LoadVideoWithFilename`、`easy framesEditor`、`LoadImage`、`easy sam3ModelLoader`、`easy sam3VideoSegmentation`、`easy sam3Visualization`、`VHS_LoadVideo`

**用到的条目**：LoadImage、workflow>面部与姿势检测、workflow>wanAnimate 采样、workflow>角色图加序号、SaveImage、SaveVideoRGBA、GetImagesFromBatchIndexed、GetVideoComponents
