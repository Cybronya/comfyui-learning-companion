---
name: text_to_image_lora_sampler_clip_273
type: Text To Image
frequency: 8
level: strong
coverage: 0.880375
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax导演台自动提示词一键生成｜图生视频省心出片_2110700731622838274.json, 视频生成/图生视频/Seedance 2.0 Global Mini图生视频｜首尾帧4K角色一致性_2097902111764860929.json, 视频生成/图生视频/Seedance 2.0图生视频｜首尾帧双参可调，生成视频自带音频_2099906662617407490.json, 视频生成/图生视频/Seedance2.0 Global图生视频｜首尾帧4K视频生成工作流_2097815419359940610.json, 视频生成/图生视频/Wan3.0多参生视频工作流｜全模态素材参考生成_2097845652163227650.json, 视频生成/图生视频/Wan3.0多参生视频｜多图参考图生视频_2097903742090825729.json, 视频生成/图生视频/wan3.0多参考图生视频｜图生视频一键直出_2092045899554971650.json, 视频生成/图生视频/全能视频图生视频低价版6-30秒处理生成工具_2102169806098231298.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_273

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax导演台自动提示词一键生成｜图生视频省心出片_2110700731622838274.json、视频生成/图生视频/Seedance 2.0 Global Mini图生视频｜首尾帧4K角色一致性_2097902111764860929.json、视频生成/图生视频/Seedance 2.0图生视频｜首尾帧双参可调，生成视频自带音频_2099906662617407490.json、视频生成/图生视频/Seedance2.0 Global图生视频｜首尾帧4K视频生成工作流_2097815419359940610.json、视频生成/图生视频/Wan3.0多参生视频工作流｜全模态素材参考生成_2097845652163227650.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `SaveVideo` —— 7/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `RH_BytedanceSeedance20GlobalImageToVideo` —— 2/8 个有
- `INTConstant` —— 1/8 个有
- `RH_BytedanceSeedance20GlobalMiniImageToVideo` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `RH_RhartVideoGImageToVideo` —— 1/8 个有
- `easy saveText` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
