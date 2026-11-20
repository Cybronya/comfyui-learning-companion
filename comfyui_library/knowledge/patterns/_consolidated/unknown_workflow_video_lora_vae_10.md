---
name: unknown_workflow_video_lora_vae_10
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84675
common_nodes: [GetImagesFromBatchIndexed, GetVideoComponents, Int, LoadVideo, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PreviewImage, SaveImage, SimpleMath+, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy blocker, easy indexAnything, easy int, workflow>wanAnimate 采样, workflow>背景与主体遮罩, workflow>面部与姿势检测]
problems: []
missing: []
members: [平台全量/二创_2036882195779948545.json, 平台全量/影视_2051513890638450689.json, 平台全量/影视二创系列 · 多角色主体替换_2075893530802868226.json, 视频生成/图生视频/影视二创系列 · 多角色主体替换_1998321199295922178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/二创_2036882195779948545.json、平台全量/影视_2051513890638450689.json、平台全量/影视二创系列 · 多角色主体替换_2075893530802868226.json、视频生成/图生视频/影视二创系列 · 多角色主体替换_1998321199295922178.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `Int`
- `LoadVideo`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `SaveImage`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy blocker`
- `easy indexAnything`
- `easy int`
- `workflow>wanAnimate 采样`
- `workflow>背景与主体遮罩`
- `workflow>面部与姿势检测`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `easy batchAnything` —— 3/4 个有
- `easy compare` —— 3/4 个有
- `easy convertAnything` —— 3/4 个有
- `easy forLoopEnd` —— 3/4 个有
- `easy forLoopStart` —— 3/4 个有
- `easy ifElse` —— 3/4 个有
- `easy imageConcat` —— 3/4 个有
- `easy imageScaleDownBy` —— 3/4 个有
- `easy mathInt` —— 3/4 个有
- `CLIPTextEncode` —— 2/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `CreateVideo` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `PrimitiveInt` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `SAM3_TrackPreview` —— 2/4 个有
- `SAM3_TrackToMask` —— 2/4 个有
- `SAM3_VideoTrack` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `easy framesEditor` —— 2/4 个有
- `easy sam3ModelLoader` —— 2/4 个有
- `easy sam3VideoSegmentation` —— 2/4 个有
- `easy sam3Visualization` —— 2/4 个有
- `workflow>获取对象遮罩` —— 2/4 个有
- `Any Switch (rgthree)` —— 1/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `MuyeLoadImage` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有
- `workflow>图像拼合` —— 1/4 个有
- `workflow>角色图加序号` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
