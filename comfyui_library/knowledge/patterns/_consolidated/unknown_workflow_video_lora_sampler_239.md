---
name: unknown_workflow_video_lora_sampler_239
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.900125
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CR Prompt Text, ColorMatch, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingSD3, PainterAI2V, PainterAudioCut, PathchSageAttentionKJ, PreviewAny, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2018664165719674881.json, 视频生成/图生视频/2017294835589324802.json, 视频生成/图生视频/2017509213773238274.json, 视频生成/图生视频/2016740203737653250.json, 视频生成/图生视频/2017231057254354945.json, 视频生成/图生视频/2017276416928260097.json, 音频生成/音频生成/自动生成数字人V2-OmniVoice声音设计（方言支持！）-Infinite Talk动态数字人_2041718633499467778.json, 音频生成/音频生成/自动生成数字人V3-VoxCPM2声音设计（方言文本翻译）-Infinite Talk数字人_2042769722399268866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_239

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2018664165719674881.json、视频生成/图生视频/2017294835589324802.json、视频生成/图生视频/2017509213773238274.json、视频生成/图生视频/2016740203737653250.json、视频生成/图生视频/2017231057254354945.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ColorMatch`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingSD3`
- `PainterAI2V`
- `PainterAudioCut`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 7/8 个有
- `RIFE VFI` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `easy seed` —— 7/8 个有
- `MathExpression|pysssss` —— 6/8 个有
- `easy showAnything` —— 6/8 个有
- `CastAnyToIntStringFloat` —— 5/8 个有
- `LoadAudio` —— 5/8 个有
- `RH_GetAudioDuration` —— 5/8 个有
- `SaveAudio` —— 5/8 个有
- `ImageScaleToTotalPixels` —— 3/8 个有
- `Qwen3_VQA` —— 3/8 个有
- `easy saveText` —— 3/8 个有
- `CR Text` —— 2/8 个有
- `FB_Qwen3TTSVoiceClone` —— 2/8 个有
- `WhisperSTT` —— 2/8 个有
- `AudioInfo` —— 1/8 个有
- `GetImageSizeAndCount` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有
- `LayerUtility: TextJoin` —— 1/8 个有
- `OmniVoiceVoiceDesignTTS` —— 1/8 个有
- `Qwen3TTSModelLoader` —— 1/8 个有
- `Qwen3TTSVoiceDesign` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `RunningHub_VoxCPM_Generate` —— 1/8 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/8 个有
- `ShowAnything|Mie` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 8 | 88% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 50% |
| 重绘幅度 | normal | - | 8 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，8 个样本，一致性 88%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 50%
- 重绘幅度 最常用 normal，8 个样本，一致性 88%
