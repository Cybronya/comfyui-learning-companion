---
name: unknown_workflow_video_lora_sampler_143
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.866692
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CR Prompt Text, ColorMatch, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingSD3, PainterAI2V, PainterAudioCut, PathchSageAttentionKJ, PreviewAny, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/AA--Infinite Talk动态数字人+Qwen TTS声音克隆_2017294835589324802.json, 视频生成/图生视频/AA--自动生成数字人-Infinite Talk动态数字人+Qwen TTS声音设计_2017509213773238274.json, 视频生成/图生视频/InfiniteTalk 2.1+2.2混用高动态图生视频数字人V1_2016740203737653250.json, 视频生成/图生视频/InfiniteTalk 2.1+2.2混用高动态图生视频数字人V2(动态加强)_2017231057254354945.json, 视频生成/图生视频/图加音频生视频数字人-高动态InfiniteTalk 2.1+2.2画音同步_2019801194713059330.json, 视频生成/图生视频/画音直出-图加音频生视频数字人-高动态InfiniteTalk 2.1+2.2_2019054926323781634.json, 视频生成/图生视频/（声音克隆）Infinite Talk高动态+Qwen TTS音画同步数字人全自动版V1_2017276416928260097.json, 视频生成/图生视频/（声音设计）Infinite Talk高动态+Qwen TTS音画同步数字人全自动版V1_2017275905328029697.json, 视频生成/图生视频/（自定义声音）Infinite Talk高动态+Qwen TTS音画同步数字人全自动版V1_2017275219941003265.json, 视频生成/图生视频/（贞贞版）Infinite Talk高动态+Qwen TTS音画同步数字人全自动版V1_2017267666708340738.json, 音频生成/音频生成/影视新闻数字人--真人感LongCat声音克隆--高动态Infinite Talk_2041718640755613698.json, 音频生成/音频生成/自动生成数字人V2-OmniVoice声音设计（方言支持！）-Infinite Talk动态数字人_2041718633499467778.json, 音频生成/音频生成/自动生成数字人V3-VoxCPM2声音设计（方言文本翻译）-Infinite Talk数字人_2042769722399268866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_143

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/AA--Infinite Talk动态数字人+Qwen TTS声音克隆_2017294835589324802.json、视频生成/图生视频/AA--自动生成数字人-Infinite Talk动态数字人+Qwen TTS声音设计_2017509213773238274.json、视频生成/图生视频/InfiniteTalk 2.1+2.2混用高动态图生视频数字人V1_2016740203737653250.json、视频生成/图生视频/InfiniteTalk 2.1+2.2混用高动态图生视频数字人V2(动态加强)_2017231057254354945.json、视频生成/图生视频/图加音频生视频数字人-高动态InfiniteTalk 2.1+2.2画音同步_2019801194713059330.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ColorMatch`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
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
- `easy cleanGpuUsed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `RIFE VFI` —— 11/13 个有
- `CastAnyToIntStringFloat` —— 9/13 个有
- `MathExpression|pysssss` —— 9/13 个有
- `RH_GetAudioDuration` —— 9/13 个有
- `SaveAudio` —— 9/13 个有
- `easy showAnything` —— 9/13 个有
- `LoadAudio` —— 8/13 个有
- `ImageScaleToTotalPixels` —— 3/13 个有
- `Qwen3_VQA` —— 3/13 个有
- `easy saveText` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `FB_Qwen3TTSCustomVoice` —— 2/13 个有
- `FB_Qwen3TTSVoiceClone` —— 2/13 个有
- `PreviewAudio` —— 2/13 个有
- `RH_LLMAPI_Pro_Node` —— 2/13 个有
- `SimpleMath+` —— 2/13 个有
- `WhisperSTT` —— 2/13 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/13 个有
- `LayerUtility: TextJoin` —— 1/13 个有
- `LongCatVoiceCloneTTS` —— 1/13 个有
- `NormalizeAudioLoudness` —— 1/13 个有
- `OmniVoiceVoiceDesignTTS` —— 1/13 个有
- `Qwen3ASRLoader` —— 1/13 个有
- `Qwen3ASRTranscribe` —— 1/13 个有
- `Qwen3TTSModelLoader` —— 1/13 个有
- `Qwen3TTSVoiceDesign` —— 1/13 个有
- `RunningHub_VoxCPM_Generate` —— 1/13 个有
- `RunningHub_VoxCPM_LoadModel` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 13 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 13 | 100% |
| 采样算法 | 1 | 1 - 1 | 13 | 100% |
| 调度器 | dpmpp_sde | - | 13 | 62% |
| 重绘幅度 | normal | - | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，13 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 调度器 最常用 dpmpp_sde，13 个样本，一致性 62%
- 重绘幅度 最常用 normal，13 个样本，一致性 100%
