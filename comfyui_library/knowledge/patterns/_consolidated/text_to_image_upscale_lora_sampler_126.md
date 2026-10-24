---
name: text_to_image_upscale_lora_sampler_126
type: Text To Image
frequency: 2
level: weak
coverage: 0.944
common_nodes: [CFGNorm, CLIPTextEncode, ClipLoaderGGUF, ConditioningZeroOut, EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoaderGGUF, LoraLoaderModelOnly, SaveImage, UpscaleModelLoader, VAEDecode, VaeGGUF]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/4G-6G显存低配电脑qwen-image高质量冰箱贴出图工作流含两次图像放大_2054808047003947010.json, 图片生成/文生图/千问提示词反推直出生图工作流_2064246942422622210.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_126

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/4G-6G显存低配电脑qwen-image高质量冰箱贴出图工作流含两次图像放大_2054808047003947010.json、图片生成/文生图/千问提示词反推直出生图工作流_2064246942422622210.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPTextEncode`
- `ClipLoaderGGUF`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoaderGGUF`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VaeGGUF`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有
- `孤海注释` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 684 | - | 2 | 50% |
| 高度 | 832 | - | 2 | 77% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 684，样本不足，未给区间，2 个样本
- 高度 中位数 832，样本不足，未给区间，2 个样本
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
