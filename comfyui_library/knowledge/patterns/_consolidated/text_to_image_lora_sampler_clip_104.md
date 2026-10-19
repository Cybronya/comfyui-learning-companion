---
name: text_to_image_lora_sampler_clip_104
type: Text To Image
frequency: 9
level: strong
coverage: 0.867111
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Ref2AV八步加速V2｜MInimaxH3 bf16-lightx2v图生视频_2094721166920478721.json, 视频生成/图生视频/T6全参官方指南｜minimaxh3自动扩展提示词分镜出图_2094333256052334594.json, 视频生成/图生视频/T8全参官方指南｜minimaxh3扩展提示词角色一致性生视频_2094463893199482882.json, 视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json, 视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词_2086537843907846146.json, 视频生成/图生视频/全参连续帧优化｜minimaxh3提示词自动图生视频生成_2094719853226717186.json, 视频生成/图生视频/古装美女扮相图生视频｜古风人像一键动起来_2098703419811909633.json, 视频生成/文生视频/双重加速）LoRA图生视频（SageAttentionMiniMax_2086535926196555778.json, 视频生成/文生视频/双重加速）LoRA文生视频（SageAttentionMiniMax_2086536536149028866.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_104

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Ref2AV八步加速V2｜MInimaxH3 bf16-lightx2v图生视频_2094721166920478721.json、视频生成/图生视频/T6全参官方指南｜minimaxh3自动扩展提示词分镜出图_2094333256052334594.json、视频生成/图生视频/T8全参官方指南｜minimaxh3扩展提示词角色一致性生视频_2094463893199482882.json、视频生成/图生视频/minimaxH3开源版首尾帧｜8step加速图生视频_2095261239302774785.json、视频生成/图生视频/minimaxh3全参官方指南自动扩展提示词_2086537843907846146.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 8/9 个有
- `LoadImage` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `Text` —— 6/9 个有
- `VHS_VideoCombine` —— 6/9 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 5/9 个有
- `ImageConcatenateMulti_UTK` —— 4/9 个有
- `LoraLoaderBypassModelOnly` —— 4/9 个有
- `MiniMaxH3ImageToVideo` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `RHHiddenNodes` —— 4/9 个有
- `CreateVideo` —— 3/9 个有
- `SaveVideo` —— 3/9 个有
- `easy showAnything` —— 3/9 个有
- `EnhancedLoadDiffusionModel` —— 2/9 个有
- `RH_Captioner` —— 2/9 个有
- `TextConcatenate_UTK` —— 2/9 个有
- `LoadAudio` —— 1/9 个有
- `easy imageSplitGrid` —— 1/9 个有
- `easy indexAnything` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 9 | 100% |
| 高度 | 80 | 80 - 80 | 9 | 100% |
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 100% |
| 调度器 | beta | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 100%
- 调度器 最常用 beta，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
