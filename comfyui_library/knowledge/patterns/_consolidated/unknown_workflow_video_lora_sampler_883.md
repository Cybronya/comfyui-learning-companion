---
name: unknown_workflow_video_lora_sampler_883
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.882
common_nodes: [1hew_AudioDuration, 1hew_ImageGridSplit, 1hew_SaveVideo, AudioAdjustVolume, AudioConcatenate, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_IntToFloat, CR Text, DF_Integer, EmptyAudio, Fast Muter (rgthree), GetNode, GetVideoComponents, HunyuanVideoFoley, If ANY execute A else B, ImageResizeKJ, ImpactInt, JWString, JWStringGetLine, JWStringSplit, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, PreviewImage, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Gemini31Flash, RIFE VFI, RunningHub SoulX-FlashHead Loader, RunningHub SoulX-FlashHead Sampler, SetNode, ShowText, StringComparison, Textbox, TrimAudio, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideoPath, VHS_MergeImages, VHS_VideoCombine, VideoCombineNode, WanFirstMiddleLastFrameToVideo, easy imageCount, easy mathFloat, easy mathInt, easy setNode, easy showAnything, string_util_StrFind, wanBlockSwap]
problems: []
missing: []
members: [视频生成/图生视频/2039676323769094146.json, 视频生成/文生视频/三分镜叙事长视频支持独白Gemini首中尾控制+WAN22REMIXV3+VBVR_2047523202926125058.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_883

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2039676323769094146.json、视频生成/文生视频/三分镜叙事长视频支持独白Gemini首中尾控制+WAN22REMIXV3+VBVR_2047523202926125058.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `1hew_AudioDuration`
- `1hew_ImageGridSplit`
- `1hew_SaveVideo`
- `AudioAdjustVolume`
- `AudioConcatenate`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `CR Text`
- `DF_Integer`
- `EmptyAudio`
- `Fast Muter (rgthree)`
- `GetNode`
- `GetVideoComponents`
- `HunyuanVideoFoley`
- `If ANY execute A else B`
- `ImageResizeKJ`
- `ImpactInt`
- `JWString`
- `JWStringGetLine`
- `JWStringSplit`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Gemini31Flash`
- `RIFE VFI`
- `RunningHub SoulX-FlashHead Loader`
- `RunningHub SoulX-FlashHead Sampler`
- `SetNode`
- `ShowText`
- `StringComparison`
- `Textbox`
- `TrimAudio`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideoPath`
- `VHS_MergeImages`
- `VHS_VideoCombine`
- `VideoCombineNode`
- `WanFirstMiddleLastFrameToVideo`
- `easy imageCount`
- `easy mathFloat`
- `easy mathInt`
- `easy setNode`
- `easy showAnything`
- `string_util_StrFind`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Apply Whisper` —— 1/2 个有
- `AudioCrop` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `Qwen3TTSModelLoader` —— 1/2 个有
- `Qwen3TTSVoiceClone` —— 1/2 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/2 个有
- `RunningHub_VoxCPM_MultiSpeaker` —— 1/2 个有
- `StringLength` —— 1/2 个有
- `TextBox` —— 1/2 个有
- `TextBoxMira` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
