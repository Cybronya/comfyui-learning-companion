---
name: unknown_workflow_controlnet_video_lora_32
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.60625
common_nodes: [Anything Everywhere, CR Prompt Text, CreateCFGScheduleFloatList, FloatConstant, GetNode, INTConstant, ImageResizeKJ, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, PrimitiveInt, Seed (rgthree), SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/04-04-01-WAN2.2-Uni3C+运镜控制图生视频_1990968895060254722.json, 视频生成/图生视频/04-04-02-WAN2.2-Uni3C+Omniconsistency转绘_1990968940883025922.json, 视频生成/图生视频/wan2.2图片反推+镜头控制_2000506448629166082.json, 视频生成/图生视频/天蝎猫--wan2.2图片反推+镜头控制_2002900702877892610.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_32

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/04-04-01-WAN2.2-Uni3C+运镜控制图生视频_1990968895060254722.json、视频生成/图生视频/04-04-02-WAN2.2-Uni3C+Omniconsistency转绘_1990968940883025922.json、视频生成/图生视频/wan2.2图片反推+镜头控制_2000506448629166082.json、视频生成/图生视频/天蝎猫--wan2.2图片反推+镜头控制_2002900702877892610.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 4 个 workflow 都包含：
- `Anything Everywhere`
- `CR Prompt Text`
- `CreateCFGScheduleFloatList`
- `FloatConstant`
- `GetNode`
- `INTConstant`
- `ImageResizeKJ`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `PrimitiveInt`
- `Seed (rgthree)`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `Text Multiline (Code Compatible)` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `RH_Jimeng_Image2Video_V2` —— 1/4 个有
- `RunningHub OmniConsistency LoraLoader` —— 1/4 个有
- `RunningHub OmniConsistency Sampler` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `VideoLoader` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
