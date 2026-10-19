---
name: unknown_workflow_video_lora_vae_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.767
common_nodes: [Any Switch (rgthree), Fast Groups Muter (rgthree), GetImagesFromBatchIndexed, GetVideoComponents, Int, LoadVideo, LoadWanVideoT5TextEncoder, MuyeLoadImage, OnnxDetectionModelLoader, PreviewImage, SaveImage, SimpleMath+, VHS_LoadVideo, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoVAELoader, easy blocker, easy framesEditor, easy indexAnything, easy int, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization, workflow>wanAnimate 采样, workflow>图像拼合, workflow>背景与主体遮罩, workflow>获取对象遮罩, workflow>角色图加序号, workflow>面部与姿势检测]
problems: []
missing: []
members: [数字人/数字人/游戏影视多人二创 · 第二步多人物角色替换（已知问题已修复）_2002697580251344898.json, 视频生成/图生视频/2010224538218401794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/游戏影视多人二创 · 第二步多人物角色替换（已知问题已修复）_2002697580251344898.json、视频生成/图生视频/2010224538218401794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `Int`
- `LoadVideo`
- `LoadWanVideoT5TextEncoder`
- `MuyeLoadImage`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `SaveImage`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `easy blocker`
- `easy framesEditor`
- `easy indexAnything`
- `easy int`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `easy sam3Visualization`
- `workflow>wanAnimate 采样`
- `workflow>图像拼合`
- `workflow>背景与主体遮罩`
- `workflow>获取对象遮罩`
- `workflow>角色图加序号`
- `workflow>面部与姿势检测`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `RTXVideoSuperResolution` —— 1/2 个有
- `SaveVideo` —— 1/2 个有
- `SaveVideoRGBA` —— 1/2 个有
- `VHS_VideoCombine` —— 1/2 个有
- `WanVideoLoraSelect` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
