---
name: unknown_workflow_video_lora_vae_6
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.775333
common_nodes: [Any Switch (rgthree), Fast Groups Muter (rgthree), GetImagesFromBatchIndexed, GetVideoComponents, Int, LoadWanVideoT5TextEncoder, OnnxDetectionModelLoader, PreviewImage, SimpleMath+, VHS_LoadVideo, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoVAELoader, easy framesEditor, easy int, easy sam3ModelLoader, easy sam3VideoSegmentation, easy sam3Visualization, workflow>wanAnimate 采样, workflow>图像拼合, workflow>背景与主体遮罩, workflow>获取对象遮罩, workflow>角色图加序号, workflow>面部与姿势检测]
problems: []
missing: []
members: [数字人/数字人/游戏影视多人二创 · 第二步多人物角色替换（已知问题已修复）_2002697580251344898.json, 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换影视多人二创多角色替换V2_2010224538218401794.json, 视频生成/图生视频/影视二创系列 · 多角色主体替换_1999055940060147714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/游戏影视多人二创 · 第二步多人物角色替换（已知问题已修复）_2002697580251344898.json、视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换影视多人二创多角色替换V2_2010224538218401794.json、视频生成/图生视频/影视二创系列 · 多角色主体替换_1999055940060147714.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetImagesFromBatchIndexed`
- `GetVideoComponents`
- `Int`
- `LoadWanVideoT5TextEncoder`
- `OnnxDetectionModelLoader`
- `PreviewImage`
- `SimpleMath+`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `easy framesEditor`
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
- `CreateVideo` —— 2/3 个有
- `LoadVideo` —— 2/3 个有
- `MuyeLoadImage` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `SaveVideo` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `WanVideoSetBlockSwap` —— 2/3 个有
- `WanVideoSetLoRAs` —— 2/3 个有
- `easy blocker` —— 2/3 个有
- `easy indexAnything` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `LoadVideoWithFilename` —— 1/3 个有
- `PoseDetectionOneToAllAnimation` —— 1/3 个有
- `RTXVideoSuperResolution` —— 1/3 个有
- `SaveVideoRGBA` —— 1/3 个有
- `WanVideoLoraSelect` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
