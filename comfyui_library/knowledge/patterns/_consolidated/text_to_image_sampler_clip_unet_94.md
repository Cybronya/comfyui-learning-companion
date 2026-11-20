---
name: text_to_image_sampler_clip_unet_94
type: Text To Image
frequency: 8
level: weak
coverage: 0.904875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/Moss base+sft文生图对比工作流_2111987431208742914.json, 数字人/数字人/Moss base与sft对比文生图，海报字体数字人全能测试_2112686062865829890.json, 数字人/数字人/云汐画梦二次元文生图｜动漫数字人形象创意生成_2097514674303619073.json, 数字人/数字人/动漫数字人绘画工作流｜角色形象文生图创意生成_2097516099490373633.json, 数字人/数字人/烬羽二次元风格绘画工作流｜数字人形象文生图生成_2097513169005662210.json, 视频生成/图生视频/5倍噌噌噌加速｜FLUX Nunchaku文生图生视频_2091234693151805442.json, 视频生成/图生视频/MOSS-Image JSON Layout结构化布局版，图文排版精准控制海报利器_2114454041609723905.json, 视频生成/图生视频/MOSS-Image三档加速横评版，50步原版8步DMD4步Turbo自由选_2114455764847915010.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_94

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/Moss base+sft文生图对比工作流_2111987431208742914.json、数字人/数字人/Moss base与sft对比文生图，海报字体数字人全能测试_2112686062865829890.json、数字人/数字人/云汐画梦二次元文生图｜动漫数字人形象创意生成_2097514674303619073.json、数字人/数字人/动漫数字人绘画工作流｜角色形象文生图创意生成_2097516099490373633.json、数字人/数字人/烬羽二次元风格绘画工作流｜数字人形象文生图生成_2097513169005662210.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `solarL_SaveImagesToZip` —— 7/8 个有
- `孤海注释` —— 7/8 个有
- `SkipLayerGuidanceDiTSimple` —— 4/8 个有
- `CheckpointLoaderSimple` —— 3/8 个有
- `Image Comparer (rgthree)` —— 3/8 个有
- `LoraLoader` —— 3/8 个有
- `EmptyFlux2LatentImage` —— 2/8 个有
- `ResolutionSelector` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `DualCLIPLoader` —— 1/8 个有
- `NunchakuFluxDiTLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 8 | 0% |
| 高度 | 80 | 80 - 1024 | 8 | 0% |
| 采样步数 | 4 | 4 - 50 | 8 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 3.5 - 4.5 | 8 | 92% |
| 采样算法 | er_sde | - | 8 | 88% |
| 调度器 | beta | - | 8 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 模型强度 | 0.17 | 0.1 - 0.27 | 3 | 61% |
| LoRA 文本强度 | 0.15 | 0.1 - 0.57 | 3 | 23% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，8 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 50，8 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 3.5 - 4.5，8 个样本，取值集中（一致性 92%）
- 采样算法 最常用 er_sde，8 个样本，一致性 88%
- 调度器 最常用 beta，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.17，观测区间 0.1 - 0.27，3 个样本
- LoRA 文本强度 中位数 0.15，观测区间 0.1 - 0.57，3 个样本，取值分散，一致性仅 23%
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
