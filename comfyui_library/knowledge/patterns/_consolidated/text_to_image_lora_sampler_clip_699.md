---
name: text_to_image_lora_sampler_clip_699
type: Text To Image
frequency: 2
level: weak
coverage: 0.8945
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LayerUtility: TextJoin, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingAuraFlow, NunchakuQwenImageDiTLoader, PathchSageAttentionKJ, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/漫剧人物种子一键直出三张一致性三视图图像【与本人的其他漫剧工作流使用可保持风格一致】_2056320439219220481.json, 图片生成/文生图/漫剧场景【与本人的其他漫剧工作流使用可保持风格一致】_2056332706560172034.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_699

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/漫剧人物种子一键直出三张一致性三视图图像【与本人的其他漫剧工作流使用可保持风格一致】_2056320439219220481.json、图片生成/文生图/漫剧场景【与本人的其他漫剧工作流使用可保持风格一致】_2056332706560172034.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `NunchakuQwenImageDiTLoader`
- `PathchSageAttentionKJ`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `UNETLoader` —— 1/2 个有
- `workflow>一键分离` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | - | 2 | 100% |
| 高度 | 1024 | - | 2 | 100% |
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

- 宽度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
