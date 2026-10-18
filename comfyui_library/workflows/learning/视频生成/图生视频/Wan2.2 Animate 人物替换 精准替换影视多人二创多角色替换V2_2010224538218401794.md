---
key: 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换影视多人二创多角色替换V2_2010224538218401794.json
name: Wan2.2 Animate 人物替换 精准替换影视多人二创多角色替换V2_2010224538218401794.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换影视多人二创多角色替换V2_2010224538218401794.json
hash: 235989c2cbf2b19f
coverage: 0.776316
learned_at: 2026-10-15 22:34:15
nodes: [GetVideoComponents, GetVideoComponents, GetVideoComponents, workflow>角色图加序号, GetImagesFromBatchIndexed, easy sam3ModelLoader, LoadVideo, easy sam3Visualization, WanVideoAnimateEmbeds, PreviewImage, LoadVideo, Reroute, Any Switch (rgthree), easy blocker, Note, Note, LoadVideo, workflow>角色图加序号, workflow>图像拼合, Note, Note, Note, workflow>角色图加序号, workflow>图像拼合, GetImagesFromBatchIndexed, GetImagesFromBatchIndexed, PreviewImage, PreviewImage, SaveImage, VHS_VideoInfoLoaded, Reroute, SaveVideoRGBA, workflow>图像拼合, workflow>面部与姿势检测, workflow>面部与姿势检测, workflow>面部与姿势检测, workflow>wanAnimate 采样, WanVideoAnimateEmbeds, workflow>背景与主体遮罩, workflow>wanAnimate 采样, WanVideoAnimateEmbeds, workflow>背景与主体遮罩, workflow>wanAnimate 采样, workflow>背景与主体遮罩, MuyeLoadImage, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, easy int, SimpleMath+, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, Label (rgthree), SaveVideoRGBA, SaveVideoRGBA, OnnxDetectionModelLoader, easy framesEditor, easy sam3VideoSegmentation, Note, workflow>获取对象遮罩, workflow>获取对象遮罩, workflow>获取对象遮罩, SaveVideoRGBA, Fast Groups Muter (rgthree), Any Switch (rgthree), Any Switch (rgthree), Any Switch (rgthree), VHS_LoadVideo, Int, Int, Note, WanVideoBlockSwap, easy indexAnything]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换影视多人二创多角色替换V2_2010224538218401794.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010224538218401794.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（76 个）：
- `GetVideoComponents`
- `GetVideoComponents`
- `GetVideoComponents`
- `workflow>角色图加序号`
- `GetImagesFromBatchIndexed`
- `easy sam3ModelLoader`
- `LoadVideo`
- `easy sam3Visualization`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
- `LoadVideo`
- `Reroute`
- `Any Switch (rgthree)`
- `easy blocker`
- `Note`
- `Note`
- `LoadVideo`
- `workflow>角色图加序号`
- `workflow>图像拼合`
- `Note`
- `Note`
- `Note`
- `workflow>角色图加序号`
- `workflow>图像拼合`
- `GetImagesFromBatchIndexed`
- `GetImagesFromBatchIndexed`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `VHS_VideoInfoLoaded`
- `Reroute`
- `SaveVideoRGBA`
- `workflow>图像拼合`
- `workflow>面部与姿势检测`
- `workflow>面部与姿势检测`
- `workflow>面部与姿势检测`
- `workflow>wanAnimate 采样`
- `WanVideoAnimateEmbeds`
- `workflow>背景与主体遮罩`
- `workflow>wanAnimate 采样`
- `WanVideoAnimateEmbeds`
- `workflow>背景与主体遮罩`
- `workflow>wanAnimate 采样`
- `workflow>背景与主体遮罩`
- `MuyeLoadImage`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `easy int`
- `SimpleMath+`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `Label (rgthree)`
- `SaveVideoRGBA`
- `SaveVideoRGBA`
- `OnnxDetectionModelLoader`
- `easy framesEditor`
- `easy sam3VideoSegmentation`
- `Note`
- `workflow>获取对象遮罩`
- `workflow>获取对象遮罩`
- `workflow>获取对象遮罩`
- `SaveVideoRGBA`
- `Fast Groups Muter (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `VHS_LoadVideo`
- `Int`
- `Int`
- `Note`
- `WanVideoBlockSwap`
- `easy indexAnything`

## 知识

覆盖率 **78%**（59/76）

**有卡**：`GetVideoComponents`、`workflow>角色图加序号`、`GetImagesFromBatchIndexed`、`easy sam3ModelLoader`、`LoadVideo`、`easy sam3Visualization`、`WanVideoAnimateEmbeds`、`easy blocker`、`workflow>图像拼合`、`SaveImage`、`VHS_VideoInfoLoaded`、`SaveVideoRGBA`、`workflow>面部与姿势检测`、`workflow>wanAnimate 采样`、`workflow>背景与主体遮罩`、`MuyeLoadImage`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`easy int`、`SimpleMath+`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`Label (rgthree)`、`OnnxDetectionModelLoader`、`easy framesEditor`、`easy sam3VideoSegmentation`、`workflow>获取对象遮罩`、`VHS_LoadVideo`、`Int`、`WanVideoBlockSwap`、`easy indexAnything`

**用到的条目**：workflow>面部与姿势检测、workflow>wanAnimate 采样、LoadWanVideoT5TextEncoder、WanVideoVAELoader、WanVideoSetLoRAs、WanVideoLoraSelectMulti、workflow>角色图加序号、SaveImage
