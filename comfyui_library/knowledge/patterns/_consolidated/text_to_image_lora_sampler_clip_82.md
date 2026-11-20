---
name: text_to_image_lora_sampler_clip_82
type: Text To Image
frequency: 15
level: strong
coverage: 0.888333
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MiniMax H3 Native vs DMAD文生视频工作流，文生视频图生视频方案_2106848580148482050.json, 视频生成/文生视频/MiniMax H3文生视频加速版 官方Turbo加速出片_2099198028581265410.json, 视频生成/文生视频/MiniMax H3文生视频基础版｜一句话生成高质量视频片段_2099177157141553154.json, 视频生成/文生视频/MiniMax H3文生视频官方版｜高质量视频生成_2095959827330723842.json, 视频生成/文生视频/MiniMax H3文生视频纯净版｜从零开始生成完整短片_2107694082242990081.json, 视频生成/文生视频/MiniMax H3文生视频｜官方加速版工作流生成_2096331392543191041.json, 视频生成/文生视频/MiniMax H3超级加速文生视频，角色一致性角色表演视频生成方案_2103903431479095298.json, 视频生成/文生视频/MiniMaxH3文生视频 文本转视频高速生成处理工具_2113771189691830274.json, 视频生成/文生视频/MiniMaxH3文生视频工作流｜文字描述直接生成精彩视频_2113557011672686593.json, 视频生成/文生视频/Minimax H3潜空间放大FL2VA版｜文生图生视频工作流_2097781976299294722.json, 视频生成/文生视频/REF2VA-Upscale双采样｜MiniMax_H3视频生成角色表演_2092872749298569217.json, 视频生成/文生视频/latent upscale潜空间放大｜Minimax H3 FL2VA版_2091024845919313921.json, 视频生成/文生视频/低动态真实感人物视频｜H3 sigma强化潜空间双采_2096336928575680513.json, 视频生成/文生视频/全能参考练习模式｜H3文生图生视频一键生成_2093263366285512706.json, 视频生成/文生视频/极速4分钟生成10秒视频｜海螺H3全能参考生视频_2091015558560047105.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_82

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 Native vs DMAD文生视频工作流，文生视频图生视频方案_2106848580148482050.json、视频生成/文生视频/MiniMax H3文生视频加速版 官方Turbo加速出片_2099198028581265410.json、视频生成/文生视频/MiniMax H3文生视频基础版｜一句话生成高质量视频片段_2099177157141553154.json、视频生成/文生视频/MiniMax H3文生视频官方版｜高质量视频生成_2095959827330723842.json、视频生成/文生视频/MiniMax H3文生视频纯净版｜从零开始生成完整短片_2107694082242990081.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 14/15 个有
- `PrimitiveFloat` —— 14/15 个有
- `ResolutionSelector` —— 14/15 个有
- `CreateVideo` —— 12/15 个有
- `SaveVideo` —— 12/15 个有
- `MiniMaxH3ImageToVideo` —— 11/15 个有
- `LTXVSeparateAVLatent` —— 7/15 个有
- `PrimitiveBoolean` —— 7/15 个有
- `LTXVConcatAVLatent` —— 6/15 个有
- `VHS_VideoCombine` —— 6/15 个有
- `ComfySwitchNode` —— 5/15 个有
- `LoadImage` —— 5/15 个有
- `ManualSigmas` —— 5/15 个有
- `PrimitiveInt` —— 5/15 个有
- `SaveImage` —— 5/15 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/15 个有
- `MiniMaxH3ReferenceToVideo` —— 4/15 个有
- `MiniMaxH3SigmaShift` —— 4/15 个有
- `MinimaxH3LatentUpscaler3D` —— 4/15 个有
- `ModelAttentionBackend` —— 4/15 个有
- `PrimitiveStringMultiline` —— 4/15 个有
- `SplitSigmas` —— 4/15 个有
- `AnyBooleanSwitch` —— 2/15 个有
- `PathchSageAttentionKJ` —— 2/15 个有
- `Seed (rgthree)` —— 2/15 个有
- `AddLabel` —— 1/15 个有
- `CR Text` —— 1/15 个有
- `H3SigmaRefiner` —— 1/15 个有
- `ImageConcanate` —— 1/15 个有
- `PainterVRAM` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 15 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 15 | 100% |
| 采样算法 | er_sde | - | 15 | 100% |
| 调度器 | beta | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |
| 宽度 | 80 | 80 - 80 | 15 | 100% |
| 高度 | 80 | 80 - 80 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，15 个样本，一致性 100%
- 调度器 最常用 beta，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，15 个样本，取值集中（一致性 100%）
- 高发问题（15/15 个样本）：Steps较低可能导致细节不足
