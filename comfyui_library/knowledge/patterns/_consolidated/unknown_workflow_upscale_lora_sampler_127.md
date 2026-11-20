---
name: unknown_workflow_upscale_lora_sampler_127
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.81
common_nodes: [EmptyLatentImage, ImageUpscaleWithModel, KSampler, LoraLoader, MZ_ChatGLM3Loader, MZ_ChatGLM3_V2, MZ_KolorsUNETLoaderV2, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Kolors文生图-自动扩写提示词-高清修复_1914333593823342594.json, 平台全量/Kolors模型+LoRA_1825789548247822338.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_127

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Kolors文生图-自动扩写提示词-高清修复_1914333593823342594.json、平台全量/Kolors模型+LoRA_1825789548247822338.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `EmptyLatentImage`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoraLoader`
- `MZ_ChatGLM3Loader`
- `MZ_ChatGLM3_V2`
- `MZ_KolorsUNETLoaderV2`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `CLIPLoader` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_Prompter` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 27.5 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 4.25 | - | 2 | 82% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | ddim_uniform | - | 2 | 50% |
| 重绘幅度 | 0.375 | - | 2 | 80% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 1152 | - | 2 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 27.5，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 4.25，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 ddim_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 0.375，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1152，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
