---
name: text_to_image_lora_sampler_clip_144
type: Text To Image
frequency: 11
level: strong
coverage: 0.885545
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/4步加速5秒3分钟｜MiniMax H3图生视频工作流_2087213237464031233.json, 视频生成/图生视频/FL2VA图生视频V2优化版｜MiniMax H3人物场景特效_2089026447229931522.json, 视频生成/图生视频/FL2VA首帧生视频荒星远征｜MiniMax H3战斗特效场景特效图生视频_2089698966752546818.json, 视频生成/图生视频/Fast图生视频加速生成｜Seedance2.0快速出片_2095868810497708034.json, 视频生成/图生视频/Seedance 2.0 Fast 图生视频｜快速把静态图变成动态大片_2097508127116718081.json, 视频生成/图生视频/Seedance 2.0 Global Mini图生视频｜首尾帧4K角色一致性_2097902111764860929.json, 视频生成/图生视频/Seedance2.0 Fast图生视频｜一张图快速动起来 速度效果两不误_2105498105788583937.json, 视频生成/图生视频/Seedance2.0 Fast图生视频｜快速高质量生成_2095608915806482433.json, 视频生成/文生视频/RuningHub企业版Seedance2.0｜图生视频视频生视频一键生成_2094303698901102593.json, 视频生成/文生视频/RuningHub企业版不降智｜Seedance2.0图生视频秒出大片_2090829853393244162.json, 视频生成/文生视频/Seedance2.0 企业版图生视频 不降智不排队可传真人照_2094167174255570946.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_144

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/4步加速5秒3分钟｜MiniMax H3图生视频工作流_2087213237464031233.json、视频生成/图生视频/FL2VA图生视频V2优化版｜MiniMax H3人物场景特效_2089026447229931522.json、视频生成/图生视频/FL2VA首帧生视频荒星远征｜MiniMax H3战斗特效场景特效图生视频_2089698966752546818.json、视频生成/图生视频/Fast图生视频加速生成｜Seedance2.0快速出片_2095868810497708034.json、视频生成/图生视频/Seedance 2.0 Fast 图生视频｜快速把静态图变成动态大片_2097508127116718081.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `RH_RhartVideoSparkvideo20FastImageToVideo` —— 7/11 个有
- `ComfyMathExpression` —— 2/11 个有
- `workflow>参数调整组` —— 2/11 个有
- `workflow>工作节点组` —— 2/11 个有
- `DF_Text_Box` —— 1/11 个有
- `Float` —— 1/11 个有
- `RH_BytedanceSeedance20GlobalMiniImageToVideo` —— 1/11 个有
- `workflow>H3-4S` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
