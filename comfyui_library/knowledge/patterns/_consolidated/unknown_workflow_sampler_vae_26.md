---
name: unknown_workflow_sampler_vae_26
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9137
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, VAELoader]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/图生图/qwen千问2509 多图编辑  加速版（4步）_1997547051980361729.json, 图片生成/图生图/qwen千问2509 多图编辑_1997529016326361089.json, 图片生成/图生图/与财神握手LoRA——Qwen-Image-Edit应用_1960877013387153409.json, 图片生成/图生图/人或者物铜像化——Qwen-Image-Edit的LoRA应用_1958111693622693889.json, 图片生成/图生图/人物图像拼合_2042497116639076354.json, 图片生成/图生图/图生图_2057815724835565569.json, 图片生成/文生图/2030304000674893825.json, 图片生成/文生图/兵马俑LoRA——Qwen-Image-Edit应用_1963214327899721729.json, 视频生成/图生视频/千问多图融合编辑_1982020667237384193.json, 视频生成/图生视频/手办LoRA——Qwen-Image-Edit应用_1961983511181856769.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_26

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/qwen千问2509 多图编辑  加速版（4步）_1997547051980361729.json、图片生成/图生图/qwen千问2509 多图编辑_1997529016326361089.json、图片生成/图生图/与财神握手LoRA——Qwen-Image-Edit应用_1960877013387153409.json、图片生成/图生图/人或者物铜像化——Qwen-Image-Edit的LoRA应用_1958111693622693889.json、图片生成/图生图/人物图像拼合_2042497116639076354.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `VAEDecode` —— 9/10 个有
- `TextEncodeQwenImageEditPlus` —— 6/10 个有
- `TextEncodeQwenImageEdit` —— 5/10 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/10 个有
- `ImageResize+` —— 2/10 个有
- `AddLabel` —— 1/10 个有
- `NunchakuQwenImageDiTLoader` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `VAEDecodeTiled` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 864 - 1280 | 10 | 91% |
| 高度 | 1152 | 768 - 1536 | 10 | 80% |
| 采样步数 | 4 | 4 - 20 | 10 | 20% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 10 | 61% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 1/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 1024，观测区间 864 - 1280，10 个样本，取值集中（一致性 91%）
- 高度 中位数 1152，观测区间 768 - 1536，10 个样本
- 采样步数 中位数 4，观测区间 4 - 20，10 个样本，取值分散，一致性仅 20%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
