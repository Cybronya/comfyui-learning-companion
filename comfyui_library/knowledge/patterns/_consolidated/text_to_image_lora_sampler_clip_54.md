---
name: text_to_image_lora_sampler_clip_54
type: Text To Image
frequency: 18
level: strong
coverage: 0.818056
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMaxH3首尾帧图生视频模板｜图生视频快速生成_2090429460284796930.json, 视频生成/图生视频/MiniMax_H3 I2V加速多参考生视频，高效图生视频工具_2110532068039028738.json, 视频生成/图生视频/MiniMax_H3_I2V加速多参考生视频，高效图生视频工具_2111269686322225154.json, 视频生成/图生视频/MiniMax_H3_I2V加速多参考视频生成工作流，图生视频高效创作工具_2109863281748963329.json, 视频生成/图生视频/MiniMax_H3_I2V加速首尾帧工作流，图生视频高效创作工具_2110535989906202626.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频图生视频与视频生视频全能参考方案_2109448439166750721.json, 视频生成/图生视频/MiniMax_H3多图参考生成视频，图生视频与视频生视频全能参考方案_2106558188098248705.json, 视频生成/图生视频/MiniMax_H3开源版首尾帧8步加速工作流，数字人图生视频处理工具_2109441379188436993.json, 视频生成/图生视频/MiniMax参考生视频视频生视频图生视频_2086540228310945793.json, 视频生成/图生视频/MiniMax多参考生成视频R2V图生视频处理工具_2102478493312442370.json, 视频生成/图生视频/Minimax H3 Veda稀疏注意力8步极速版首尾帧 视频生成控制_2108993138235895809.json, 视频生成/图生视频/MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425.json, 视频生成/图生视频/Minimax多参考生成视频R2V工作流，最多9张参考图3段参考视频方案_2106851933465169922.json, 视频生成/图生视频/Minimax多参考生成视频R2V工作流，最多9张参考图3段参考视频方案_2110209158552317953.json, 视频生成/图生视频/Minimax多参考生视频R2V，9张参考图3段视频方案_2110867933206503425.json, 视频生成/图生视频/Minmax R2V参考生视频｜多图参考图生视频一键出片｜视频创作利器_2102208736826847234.json, 视频生成/图生视频/Minmax多参考生成视频R2V 多模态输入视频生成方案_2108651204296400897.json, 视频生成/图生视频/Minmax多参考生视频R2V，视频生视频多图精准控制_2111190495966883841.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_54

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3首尾帧图生视频模板｜图生视频快速生成_2090429460284796930.json、视频生成/图生视频/MiniMax_H3 I2V加速多参考生视频，高效图生视频工具_2110532068039028738.json、视频生成/图生视频/MiniMax_H3_I2V加速多参考生视频，高效图生视频工具_2111269686322225154.json、视频生成/图生视频/MiniMax_H3_I2V加速多参考视频生成工作流，图生视频高效创作工具_2109863281748963329.json、视频生成/图生视频/MiniMax_H3_I2V加速首尾帧工作流，图生视频高效创作工具_2110535989906202626.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 17/18 个有
- `PrimitiveStringMultiline` —— 16/18 个有
- `SaveImage` —— 15/18 个有
- `孤海注释` —— 12/18 个有
- `MiniMaxH3ReferenceToVideo` —— 11/18 个有
- `PreviewImage` —— 10/18 个有
- `ComfySwitchNode` —— 9/18 个有
- `EmptyImage` —— 9/18 个有
- `LoadAudio` —— 9/18 个有
- `PrimitiveBoolean` —— 9/18 个有
- `PrimitiveInt` —— 9/18 个有
- `VHS_LoadVideo` —— 8/18 个有
- `GetNode` —— 7/18 个有
- `MiniMaxH3ImageToVideo` —— 7/18 个有
- `SetNode` —— 7/18 个有
- `AudioCrop` —— 2/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/18 个有
- `easy minimaxH3AudioLock` —— 2/18 个有
- `AnySwitch` —— 1/18 个有
- `Fast Bypasser (rgthree)` —— 1/18 个有
- `GetVideoComponents` —— 1/18 个有
- `INTConstant` —— 1/18 个有
- `ImageResizeKJv2` —— 1/18 个有
- `LoadVideo` —— 1/18 个有
- `MiniMaxH3SaveLatent` —— 1/18 个有
- `PreviewAny` —— 1/18 个有
- `QwenH3PromptLocal` —— 1/18 个有
- `Seed (rgthree)` —— 1/18 个有
- `Text Multiline` —— 1/18 个有
- `VedaSparseAttention` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（23/18 个样本）：Steps较低可能导致细节不足
