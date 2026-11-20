---
name: unknown_workflow_sampler_vae_34
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.857727
common_nodes: [CLIPLoader, KSampler, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Nunchaku-qwen image文生图_1965030044580069377.json, 图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json, 图片生成/文生图/Nunchaku超级加速 Qwen Image文生图_1966409848168624130.json, 图片生成/文生图/Qwen Image+Lora文生图-K采样器版本_1955444043092299778.json, 图片生成/文生图/Qwen Image+双Lora文生图- 双K采样器版本_1955600731353989122.json, 图片生成/文生图/千问文生图+双节棍（Qwen Nunchaku）_1964286433756332033.json, 图片生成/文生图/千问文生图极速生图双节棍 Qwen Nunchaku_1968509624422944769.json, 图片生成/文生图/服装_床品_地毯花纹一键提取！QwenImageEdit2511工作流详解，小白友好+全节点注释_2059565759478718465.json, 图片生成/文生图/设计师必备ComfyUI工作流：实物照片→干净印花，全节点手把手注释_2059565790445260801.json, 平台全量/印花提取YinHuaTiQu-Qwen-Image-Edit工作流V2_2511_2009984765469925378.json, 平台全量/服装图案迁移样机Qwen-Image-Edit 迁移图像到T恤、衣服上 服装图案样板 模特试衣 服饰_1998206259205668865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_34

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Nunchaku-qwen image文生图_1965030044580069377.json、图片生成/文生图/Nunchaku1.0正式版+ Qwen-Image：速度与质量的终极平衡！文生图_1965259047710674945.json、图片生成/文生图/Nunchaku超级加速 Qwen Image文生图_1966409848168624130.json、图片生成/文生图/Qwen Image+Lora文生图-K采样器版本_1955444043092299778.json、图片生成/文生图/Qwen Image+双Lora文生图- 双K采样器版本_1955600731353989122.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 9/11 个有
- `CFGNorm` —— 8/11 个有
- `CLIPTextEncode` —— 7/11 个有
- `LoraLoader` —— 6/11 个有
- `UNETLoader` —— 6/11 个有
- `LoadImage` —— 5/11 个有
- `NunchakuQwenImageDiTLoader` —— 5/11 个有
- `TextEncodeQwenImageEditPlus` —— 4/11 个有
- `JjkText` —— 3/11 个有
- `Text` —— 3/11 个有
- `CR SDXL Aspect Ratio` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 30 | 11 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 11 | 43% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 73% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 1.25 | 1 - 1.5 | 6 | 80% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 30，11 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，11 个样本，取值分散，一致性仅 43%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 73%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1.25，观测区间 1 - 1.5，6 个样本，取值集中（一致性 80%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/11 个样本）：Steps较低可能导致细节不足
