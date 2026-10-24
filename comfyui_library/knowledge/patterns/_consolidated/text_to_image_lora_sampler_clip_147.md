---
name: text_to_image_lora_sampler_clip_147
type: Text To Image
frequency: 11
level: strong
coverage: 0.886
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3 上下文参考视频+图生视频｜融合运镜与角色_2096868508067000322.json, 视频生成/图生视频/MiniMax H3上下文多参考生视频 多图融合创作_2098822713052844033.json, 视频生成/图生视频/MiniMax H3两段式管线｜图生视频高清直出_2098701054606135298.json, 视频生成/图生视频/MiniMax_H3上下文参考视频加图生视频｜融合运镜与角色一致性_2101908397733011457.json, 视频生成/图生视频/Seedance 2.0图生视频｜首尾帧双参可调，生成视频自带音频_2099906662617407490.json, 视频生成/图生视频/Seedance2.0 Global图生视频｜首尾帧4K视频生成工作流_2097815419359940610.json, 视频生成/图生视频/Wan3.0多参生视频工作流｜全模态素材参考生成_2097845652163227650.json, 视频生成/图生视频/wan3.0多参考图生视频｜图生视频一键直出_2092045899554971650.json, 视频生成/图生视频/上下文参考视频融合运镜｜MiniMax H3角色一致性图生视频_2096676491013742593.json, 视频生成/图生视频/动作迁移角色替换AI视频换人｜免改骨架直接换主角｜图生视频_2101892897812606978.json, 视频生成/图生视频/视频修复增强｜去噪清晰化画质提升，老片翻新必备_2101226303985901570.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_147

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3 上下文参考视频+图生视频｜融合运镜与角色_2096868508067000322.json、视频生成/图生视频/MiniMax H3上下文多参考生视频 多图融合创作_2098822713052844033.json、视频生成/图生视频/MiniMax H3两段式管线｜图生视频高清直出_2098701054606135298.json、视频生成/图生视频/MiniMax_H3上下文参考视频加图生视频｜融合运镜与角色一致性_2101908397733011457.json、视频生成/图生视频/Seedance 2.0图生视频｜首尾帧双参可调，生成视频自带音频_2099906662617407490.json…）

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
- `LoraLoaderModelOnly`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 10/11 个有
- `LoadImage` —— 8/11 个有
- `PrimitiveStringMultiline` —— 6/11 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 4/11 个有
- `RH_MinimaxHailuoH3MultimodalToVideo` —— 4/11 个有
- `EmptyImage` —— 3/11 个有
- `LoadVideo` —— 3/11 个有
- `PreviewImage` —— 3/11 个有
- `RH_AlibabaWan30ReferenceToVideo` —— 2/11 个有
- `RH_BytedanceSeedance20GlobalImageToVideo` —— 2/11 个有
- `RH_TopazLabs_VideoUpscale` —— 2/11 个有
- `SaveImage` —— 2/11 个有
- `RHBerniniFullReferenceVideoToVideo` —— 1/11 个有
- `RH_MinimaxHailuoH3ImageToVideo` —— 1/11 个有

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
