---
name: text_to_image_lora_sampler_clip_81
type: Text To Image
frequency: 12
level: strong
coverage: 0.863083
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, MiniMaxH3ImageToVideo, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3 Native vs DMAD文生视频工作流，文生视频图生视频方案_2106848580148482050.json, 视频生成/文生视频/MiniMax H3文生视频 官方全模态立体声生成_2098835843896139777.json, 视频生成/文生视频/MiniMax H3文生视频加速版 官方Turbo加速出片_2099198028581265410.json, 视频生成/文生视频/MiniMax H3文生视频基础版｜一句话生成高质量视频片段_2099177157141553154.json, 视频生成/文生视频/MiniMax H3文生视频官方版｜高质量视频生成_2095959827330723842.json, 视频生成/文生视频/MiniMax H3文生视频纯净版｜从零开始生成完整短片_2107694082242990081.json, 视频生成/文生视频/MiniMax H3文生视频｜官方加速版工作流生成_2096331392543191041.json, 视频生成/文生视频/MiniMax H3超级加速文生视频，角色一致性角色表演视频生成方案_2103903431479095298.json, 视频生成/文生视频/Minimax_h3超级加速文生视频｜角色一致表演流畅省币首选_2103681865688375297.json, 视频生成/文生视频/Minimax文生视频T2V工作流，加写实LoRA开关文生视频方案_2106872283892637697.json, 视频生成/文生视频/SageAttention+LoRA双重加速文生视频｜MiniMax H3文生视频工作流_2087185930007437314.json, 视频生成/文生视频/SageAttention+LoRA双重加速｜MiniMax H3文生视频_2089404463130963970.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Native vs DMAD文生视频工作流，文生视频图生视频方案_2106848580148482050.json、视频生成/文生视频/MiniMax H3文生视频 官方全模态立体声生成_2098835843896139777.json、视频生成/文生视频/MiniMax H3文生视频加速版 官方Turbo加速出片_2099198028581265410.json、视频生成/文生视频/MiniMax H3文生视频基础版｜一句话生成高质量视频片段_2099177157141553154.json、视频生成/文生视频/MiniMax H3文生视频官方版｜高质量视频生成_2095959827330723842.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `ResolutionSelector` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/12 个有
- `ComfySwitchNode` —— 5/12 个有
- `PrimitiveBoolean` —— 5/12 个有
- `PrimitiveInt` —— 5/12 个有
- `SaveImage` —— 5/12 个有
- `VHS_VideoCombine` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `LoraLoaderBypassModelOnly` —— 2/12 个有
- `PainterVRAM` —— 2/12 个有
- `Seed (rgthree)` —— 2/12 个有
- `AddLabel` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `ImageConcanate` —— 1/12 个有
- `LTXVSeparateAVLatent` —— 1/12 个有
- `MiniMaxH3SigmaShift` —— 1/12 个有
- `SetNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
