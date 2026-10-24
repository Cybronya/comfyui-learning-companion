---
name: text_to_image_sampler_clip_unet_33
type: Text To Image
frequency: 13
level: weak
coverage: 0.905692
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/9 个 Krea 2 LoRA 测试_2069657247956946945.json, 图片生成/文生图/A-15 Krea2 特定风格 人像大作 文生图_2098692058323177474.json, 图片生成/文生图/Anima强大的动漫文生图turbo高速版_2061065103197425666.json, 图片生成/文生图/Boogu 文生图极速版_2069639754718728194.json, 图片生成/文生图/Boogu-Image 0.1 Turbo 极速文生图_2067853157933338626.json, 图片生成/文生图/Boogu-Image 0.1 Turbo_2069099036728184834.json, 图片生成/文生图/Boogu-Image Turbo 文生图 极速版_2068190168858841090.json, 图片生成/文生图/Krea 2_2072697671621636097.json, 图片生成/文生图/Krea2+Turbo文生图（双采版）_2071171911891111938.json, 图片生成/文生图/Krea2-Cc测试Lora专用流_2080172818469318657.json, 图片生成/文生图/Krea2-全能文生图2K直出-MJ平替_2082660207729143809.json, 图片生成/文生图/Krea2特定风格人像大作文生图｜固定风格批量出人像大片_2099133481472315394.json, 图片生成/文生图/Qwen Image 2.1文生图加4步加速，高质量文本到图像生成工作流_2103932568507863042.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/9 个 Krea 2 LoRA 测试_2069657247956946945.json、图片生成/文生图/A-15 Krea2 特定风格 人像大作 文生图_2098692058323177474.json、图片生成/文生图/Anima强大的动漫文生图turbo高速版_2061065103197425666.json、图片生成/文生图/Boogu 文生图极速版_2069639754718728194.json、图片生成/文生图/Boogu-Image 0.1 Turbo 极速文生图_2067853157933338626.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 8/13 个有
- `LoraLoaderModelOnly` —— 7/13 个有
- `ResolutionSelector` —— 7/13 个有
- `JjkText` —— 2/13 个有
- `easy ifElse` —— 2/13 个有
- `solarL_SaveImagesToZip` —— 2/13 个有
- `孤海注释` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `CR Text` —— 1/13 个有
- `FluxResolutionNode` —— 1/13 个有
- `INTConstant` —— 1/13 个有
- `LoraLoader` —— 1/13 个有
- `ModelAttentionBackend` —— 1/13 个有
- `SaveImageAdvanced` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1280 | 13 | 57% |
| 高度 | 1024 | 80 - 1920 | 13 | 47% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 4 | 4 - 10 | 13 | 63% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 13 | 18% |
| 采样算法 | er_sde | - | 13 | 38% |
| 调度器 | simple | - | 13 | 46% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1280，13 个样本
- 高度 中位数 1024，观测区间 80 - 1920，13 个样本，取值分散，一致性仅 47%
- 采样步数 中位数 4，观测区间 4 - 10，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，13 个样本，取值分散，一致性仅 18%
- 采样算法 最常用 er_sde，13 个样本，一致性 38%
- 调度器 最常用 simple，13 个样本，一致性 46%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（28/13 个样本）：Steps较低可能导致细节不足
