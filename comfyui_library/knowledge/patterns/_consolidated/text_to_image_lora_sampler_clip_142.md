---
name: text_to_image_lora_sampler_clip_142
type: Text To Image
frequency: 12
level: strong
coverage: 0.76475
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveInt, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425.json, 视频生成/图生视频/Minimax多参考生成视频R2V工作流，最多9张参考图3段参考视频方案_2106851933465169922.json, 视频生成/图生视频/Minimax多参考生成视频R2V工作流，最多9张参考图3段参考视频方案_2110209158552317953.json, 视频生成/图生视频/Minimax多参考生视频R2V，9张参考图3段视频方案_2110867933206503425.json, 视频生成/图生视频/Minmax R2V参考生视频｜多图参考图生视频一键出片｜视频创作利器_2102208736826847234.json, 视频生成/图生视频/Minmax多参考生成视频R2V 多模态输入视频生成方案_2108651204296400897.json, 视频生成/图生视频/Minmax多参考生视频R2V，视频生视频多图精准控制_2111190495966883841.json, 视频生成/图生视频/h3参考生视频方案，图生视频多参考精准还原_2110861891965902849.json, 视频生成/图生视频/minimax_h3多图参考生视频｜图生视频高质量生成工作流_2097783512152760321.json, 视频生成/文生视频/Minimax文生视频T2V工作流，文生视频官方文生视频处理工具_2107930345889943553.json, 视频生成/文生视频/文图参考生视频多合一工作流｜MiniMax H3文生图生视频生视频_2087160168411910145.json, 视频生成/视频生视频/MiniMax H3参考图和参考视音频生成视频满血版，9图3视频3音频方案_2106117790418685954.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_142

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/MinimaxH3人物替换character swap，视频生视频精准换人_2110516163112423425.json、视频生成/图生视频/Minimax多参考生成视频R2V工作流，最多9张参考图3段参考视频方案_2106851933465169922.json、视频生成/图生视频/Minimax多参考生成视频R2V工作流，最多9张参考图3段参考视频方案_2110209158552317953.json、视频生成/图生视频/Minimax多参考生视频R2V，9张参考图3段视频方案_2110867933206503425.json、视频生成/图生视频/Minmax R2V参考生视频｜多图参考图生视频一键出片｜视频创作利器_2102208736826847234.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 11/12 个有
- `LoadImage` —— 11/12 个有
- `MiniMaxH3ReferenceToVideo` —— 11/12 个有
- `PrimitiveBoolean` —— 11/12 个有
- `PrimitiveStringMultiline` —— 11/12 个有
- `孤海注释` —— 11/12 个有
- `LoadAudio` —— 10/12 个有
- `SaveImage` —— 10/12 个有
- `GetNode` —— 7/12 个有
- `SetNode` —— 7/12 个有
- `VHS_LoadVideo` —— 6/12 个有
- `AudioCrop` —— 3/12 个有
- `GetVideoComponents` —— 3/12 个有
- `LoadVideo` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `easy minimaxH3AudioLock` —— 3/12 个有
- `EmptyImage` —— 2/12 个有
- `MiniMaxH3ImageToVideo` —— 2/12 个有
- `AnySwitch` —— 1/12 个有
- `Fast Bypasser (rgthree)` —— 1/12 个有
- `MiniMaxH3AddGuide` —— 1/12 个有
- `MiniMaxH3SaveLatent` —— 1/12 个有
- `PreviewAny` —— 1/12 个有
- `QwenH3PromptLocal` —— 1/12 个有
- `VideoCombineV2` —— 1/12 个有

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
| Steps较低可能导致细节不足 | 13/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（13/12 个样本）：Steps较低可能导致细节不足
