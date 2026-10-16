---
key: 视频生成/图生视频/视频二创-多角色替换Wan Animate+OneToAll+Same3+SeedVR2.5_2004211768807354370.json
name: 视频二创-多角色替换Wan Animate+OneToAll+Same3+SeedVR2.5_2004211768807354370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2004211768807354370.json
hash: d392dfd259640298
coverage: 0.779412
learned_at: 2026-10-15 22:33:53
nodes: [easy framesEditor, easy sam3Visualization, GetVideoComponents, easy sam3ModelLoader, OnnxDetectionModelLoader, VHS_VideoInfoLoaded, easy sam3VideoSegmentation, workflow>WanAnimate KJ加载器, SimpleMath+, WanVideoAnimateEmbeds, GetVideoComponents, workflow>角色图加序号, SaveVideoRGBA, WanVideoAnimateEmbeds, GetVideoComponents, workflow>角色图加序号, PreviewImage, workflow>wanAnimate 采样, workflow>wanAnimate 采样, SaveVideoRGBA, LoadVideoWithFilename, PreviewImage, workflow>背景与主体遮罩, workflow>背景与主体遮罩, workflow>获取对象遮罩, GetImagesFromBatchIndexed, workflow>图像拼合, GetImagesFromBatchIndexed, workflow>图像拼合, workflow>图像拼合, workflow>获取对象遮罩, workflow>背景与主体遮罩, workflow>获取对象遮罩, Int, Int, workflow>角色图加序号, SaveVideoRGBA, easy int, LoadImage, LoadImage, LoadImage, Fast Groups Muter (rgthree), Note, WanVideoAnimateEmbeds, workflow>wanAnimate 采样, SaveImage, Reroute, Reroute, VHS_LoadVideo, Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), SaveVideoRGBA, workflow>面部与姿势检测, Any Switch (rgthree), PoseDetectionOneToAllAnimation, workflow>面部与姿势检测, Any Switch (rgthree), workflow>面部与姿势检测, Any Switch (rgthree), Fast Groups Muter (rgthree), GetImagesFromBatchIndexed, LoadVideoWithFilename, LoadVideoWithFilename, PreviewImage, Fast Groups Muter (rgthree), PoseDetectionOneToAllAnimation, PoseDetectionOneToAllAnimation]
patterns: []
missing: []
---

# 视频生成/图生视频/视频二创-多角色替换Wan Animate+OneToAll+Same3+SeedVR2.5_2004211768807354370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004211768807354370.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（68 个）：
- `easy framesEditor`
- `easy sam3Visualization`
- `GetVideoComponents`
- `easy sam3ModelLoader`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfoLoaded`
- `easy sam3VideoSegmentation`
- `workflow>WanAnimate KJ加载器`
- `SimpleMath+`
- `WanVideoAnimateEmbeds`
- `GetVideoComponents`
- `workflow>角色图加序号`
- `SaveVideoRGBA`
- `WanVideoAnimateEmbeds`
- `GetVideoComponents`
- `workflow>角色图加序号`
- `PreviewImage`
- `workflow>wanAnimate 采样`
- `workflow>wanAnimate 采样`
- `SaveVideoRGBA`
- `LoadVideoWithFilename`
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
- `SaveVideoRGBA`
- `easy int`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `Note`
- `WanVideoAnimateEmbeds`
- `workflow>wanAnimate 采样`
- `SaveImage`
- `Reroute`
- `Reroute`
- `VHS_LoadVideo`
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
- `Fast Groups Muter (rgthree)`
- `GetImagesFromBatchIndexed`
- `LoadVideoWithFilename`
- `LoadVideoWithFilename`
- `PreviewImage`
- `Fast Groups Muter (rgthree)`
- `PoseDetectionOneToAllAnimation`
- `PoseDetectionOneToAllAnimation`

## 知识

覆盖率 **78%**（53/68）

**有卡**：`easy framesEditor`、`easy sam3Visualization`、`GetVideoComponents`、`easy sam3ModelLoader`、`OnnxDetectionModelLoader`、`VHS_VideoInfoLoaded`、`easy sam3VideoSegmentation`、`workflow>WanAnimate KJ加载器`、`SimpleMath+`、`WanVideoAnimateEmbeds`、`workflow>角色图加序号`、`SaveVideoRGBA`、`workflow>wanAnimate 采样`、`LoadVideoWithFilename`、`workflow>背景与主体遮罩`、`workflow>获取对象遮罩`、`GetImagesFromBatchIndexed`、`workflow>图像拼合`、`Int`、`easy int`、`LoadImage`、`SaveImage`、`VHS_LoadVideo`、`workflow>面部与姿势检测`、`PoseDetectionOneToAllAnimation`

**用到的条目**：LoadImage、workflow>面部与姿势检测、workflow>wanAnimate 采样、workflow>角色图加序号、SaveImage、SaveVideoRGBA、GetImagesFromBatchIndexed、GetVideoComponents
