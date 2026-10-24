---
name: image_to_image_sampler_clip_unet_170
type: Image To Image
frequency: 2
level: weak
coverage: 0.926
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptySD3LatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, PreviewAny, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen3.8+z turbo洗图_2107679352057065474.json, 图片生成/文生图/高清画质升级！Z-Imag+KREA2 双采样_2073296835644575745.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_170

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/qwen3.8+z turbo洗图_2107679352057065474.json、图片生成/文生图/高清画质升级！Z-Imag+KREA2 双采样_2073296835644575745.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `DapaoImageAspectRatioResizeNode` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `ModelPatchLoader` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `QwenImageDiffsynthControlnet` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.7 | - | 2 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
