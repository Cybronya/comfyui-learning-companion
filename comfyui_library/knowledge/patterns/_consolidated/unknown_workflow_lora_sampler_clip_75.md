---
name: unknown_workflow_lora_sampler_clip_75
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.854857
common_nodes: [ApplySageAttention, CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, EnhancedLoadDiffusionModel, GetNode, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PreviewImage, PromptRelaySmartEncode, SetNode, Text, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/本地开源免费，真人运镜长镜头9_2059271998416703490.json, 视频生成/图生视频/本地开源免费，真实运镜长镜头12_2059863423894245377.json, 视频生成/图生视频/本地开源免费，神奇lora4_2056247410921398274.json, 视频生成/图生视频/漫剧分镜视频6_2060085027895078914.json, 视频生成/图生视频/漫剧图生视频remix v3_2069004498625982466.json, 视频生成/图生视频/漫剧图生视频remixv2_2069080646349312001.json, 视频生成/图生视频/高画质版漫剧图生视频_2068991509701160961.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_75

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/本地开源免费，真人运镜长镜头9_2059271998416703490.json、视频生成/图生视频/本地开源免费，真实运镜长镜头12_2059863423894245377.json、视频生成/图生视频/本地开源免费，神奇lora4_2056247410921398274.json、视频生成/图生视频/漫剧分镜视频6_2060085027895078914.json、视频生成/图生视频/漫剧图生视频remix v3_2069004498625982466.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `ApplySageAttention`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `EnhancedLoadDiffusionModel`
- `GetNode`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PreviewImage`
- `PromptRelaySmartEncode`
- `SetNode`
- `Text`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchThief` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `PatchModelPatcherOrder` —— 4/7 个有
- `TextConcatenate_UTK` —— 4/7 个有
- `VAEEncode` —— 4/7 个有
- `WanImageToVideoSVIPro` —— 4/7 个有
- `LayerUtility: PurgeVRAM V2` —— 3/7 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 3/7 个有
- `PreviewAny` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `RegexExtract` —— 3/7 个有
- `StringReplace` —— 3/7 个有
- `Switch` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `CreateVideo` —— 1/7 个有
- `ImageBatchExtendWithOverlap` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有
- `SaveVideo` —— 1/7 个有
- `easy indexAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
