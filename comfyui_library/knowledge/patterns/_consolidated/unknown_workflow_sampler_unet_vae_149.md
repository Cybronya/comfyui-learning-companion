---
name: unknown_workflow_sampler_unet_vae_149
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.955143
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CR Prompt Text, ComfyMathExpression, EasyCache, KSamplerSelect, LoadAudio, LoadImage, MiniMaxH3ReferenceToVideo, PathchSageAttentionKJ, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/AI Video Studio PR插件VIP专用短视频最新工作流_2107706140200099841.json, 图片生成/文生图/AI Video Studio 专用短视频生成工作流_2107634472081510402.json, 视频生成/文生视频/AI Video Studio PR插件VIP专用短剧专用工作流_2103080690807037953.json, 视频生成/文生视频/AI Video Studio PR插件VIP专用短剧生成单人对口型_2095494977097916418.json, 视频生成/文生视频/AI Video Studio PR插件VIP专用短剧生成工作流_2102629858160496642.json, 视频生成/文生视频/AI Video Studio PR插件VIP专用短剧生成最新工作流_2093552366741180417.json, 视频生成/文生视频/AI Video Studio PR插件VIP专用短剧生成（多人）工作流_2095674532345499649.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_149

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/AI Video Studio PR插件VIP专用短视频最新工作流_2107706140200099841.json、图片生成/文生图/AI Video Studio 专用短视频生成工作流_2107634472081510402.json、视频生成/文生视频/AI Video Studio PR插件VIP专用短剧专用工作流_2103080690807037953.json、视频生成/文生视频/AI Video Studio PR插件VIP专用短剧生成单人对口型_2095494977097916418.json、视频生成/文生视频/AI Video Studio PR插件VIP专用短剧生成工作流_2102629858160496642.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EasyCache`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `CR Text` —— 5/7 个有
- `ImageUpscaleWithModel` —— 5/7 个有
- `LazySwitchKJ_UTK` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `TextConcatenate_UTK` —— 5/7 个有
- `UpscaleModelLoader` —— 5/7 个有
- `easy boolean` —— 5/7 个有
- `Apply Whisper` —— 4/7 个有
- `AudioCrop` —— 4/7 个有
- `DF_Int_to_Float` —— 4/7 个有
- `FB_Qwen3TTSDialogueInference` —— 4/7 个有
- `FB_Qwen3TTSRoleBank` —— 4/7 个有
- `FB_Qwen3TTSVoiceClonePrompt` —— 4/7 个有
- `ImpactSwitch` —— 4/7 个有
- `VHS_VideoCombine` —— 4/7 个有
- `CreateVideo` —— 3/7 个有
- `SaveVideo` —— 3/7 个有
- `VAEDecodeAudio` —— 3/7 个有
- `ImageScaleBy` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
