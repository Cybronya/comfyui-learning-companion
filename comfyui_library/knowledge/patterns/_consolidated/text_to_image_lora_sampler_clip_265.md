---
name: text_to_image_lora_sampler_clip_265
type: Text To Image
frequency: 8
level: weak
coverage: 0.897625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/xingtong_base_v2_2061416410592669697.json, 图片生成/文生图/剑来-大骊娘娘_2004711609975144450.json, 图片生成/文生图/动漫生图｜Anima base v1官方文生图直出_2089769718608650241.json, 图片生成/文生图/文生图Qwen2512领军模型完美中文 高质量画面直出_2109036747249246209.json, 图片生成/文生图/文生图工作流 高质量画面直出稳定出图方案_2109419687699374082.json, 图片生成/文生图/文生图工作流高质量画面直出稳定出图方案 高质量画面直出_2109747077147348994.json, 图片生成/文生图/文生图超快出图｜输入描述秒级生成高质量图片_2101533926996144130.json, 图片生成/文生图/最新qwen+image2512文生图｜基础工作流高质量出图_2095294645029920770.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_265

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/xingtong_base_v2_2061416410592669697.json、图片生成/文生图/剑来-大骊娘娘_2004711609975144450.json、图片生成/文生图/动漫生图｜Anima base v1官方文生图直出_2089769718608650241.json、图片生成/文生图/文生图Qwen2512领军模型完美中文 高质量画面直出_2109036747249246209.json、图片生成/文生图/文生图工作流 高质量画面直出稳定出图方案_2109419687699374082.json…）

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
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 6/8 个有
- `solarL_SaveImagesToZip` —— 6/8 个有
- `孤海注释` —— 6/8 个有
- `ModelSamplingAuraFlow` —— 4/8 个有
- `PrimitiveInt` —— 2/8 个有
- `Text Multiline` —— 2/8 个有
- `AddLabel` —— 1/8 个有
- `CFGNorm` —— 1/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `QwenImageLatentAspectRatio` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有
- `easy float` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 8 | 0% |
| 高度 | 80 | 80 - 1920 | 8 | 0% |
| 采样步数 | 4 | 4 - 50 | 8 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 8 | 71% |
| 采样算法 | er_sde | - | 8 | 75% |
| 调度器 | beta | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，8 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，8 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 50，8 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，8 个样本
- 采样算法 最常用 er_sde，8 个样本，一致性 75%
- 调度器 最常用 beta，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
