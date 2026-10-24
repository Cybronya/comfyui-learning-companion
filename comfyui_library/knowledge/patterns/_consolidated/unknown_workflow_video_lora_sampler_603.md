---
name: unknown_workflow_video_lora_sampler_603
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.598667
common_nodes: [CR Prompt Text, GetNode, HuMoEmbeds, ImageBatchMulti, ImageResizeKJv2, Int, JWFloat, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewImage, SetNode, SoundFlow_GetLength, SoundFlow_TrimAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WhisperModelLoader]
problems: []
missing: []
members: [视频生成/图生视频/Humo+InfiniteTalk+Lynx三分镜MV-大幅提升人物一致性_20251109_1990237934462881793.json, 视频生成/图生视频/Humo+InfiniteTalk三分镜MV_20251109_1985880552534355969.json, 视频生成/图生视频/Humo三镜头MV_20251104_1985702595668975618.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_603

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Humo+InfiniteTalk+Lynx三分镜MV-大幅提升人物一致性_20251109_1990237934462881793.json、视频生成/图生视频/Humo+InfiniteTalk三分镜MV_20251109_1985880552534355969.json、视频生成/图生视频/Humo三镜头MV_20251104_1985702595668975618.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：60%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Prompt Text`
- `GetNode`
- `HuMoEmbeds`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `JWFloat`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewImage`
- `SetNode`
- `SoundFlow_GetLength`
- `SoundFlow_TrimAudio`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WhisperModelLoader`

**可变部分**（部分 workflow 才有）：
- `MultiTalkModelLoader` —— 2/3 个有
- `MultiTalkWav2VecEmbeds` —— 2/3 个有
- `WanVideoCombineEmbeds` —— 2/3 个有
- `WanVideoImageToVideoMultiTalk` —— 2/3 个有
- `Wav2VecModelLoader` —— 2/3 个有
- `LoadLynxResampler` —— 1/3 个有
- `LynxEncodeFaceIP` —— 1/3 个有
- `LynxInsightFaceCrop` —— 1/3 个有
- `WanVideoAddLynxEmbeds` —— 1/3 个有
- `WanVideoExtraModelSelect` —— 1/3 个有
- `WanVideoSetBlockSwap` —— 1/3 个有
- `WanVideoSetLoRAs` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
