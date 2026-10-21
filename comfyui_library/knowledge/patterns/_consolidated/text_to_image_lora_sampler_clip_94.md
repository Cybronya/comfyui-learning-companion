---
name: text_to_image_lora_sampler_clip_94
type: Text To Image
frequency: 11
level: strong
coverage: 0.874727
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3首尾帧生视频｜官方加速版工作流制作_2096332861723996162.json, 视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2086208730663841794.json, 视频生成/图生视频/MiniMaxH3首尾帧图生视频模板｜图生视频快速生成_2090429460284796930.json, 视频生成/图生视频/Minimax H3图生视频Lightx2v正式版生成工作流_2088211425947897858.json, 视频生成/图生视频/Minimax H3首尾帧生视频In8加速版图生视频生成_2088209952254021634.json, 视频生成/图生视频/Minimax-H3-图生视频（Lightx2v加速）_2086209989152174082.json, 视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json, 视频生成/图生视频/MinimaxH3故事板九宫格分镜-4步加速多参考图人物场景特效_2087363609331589121.json, 视频生成/图生视频/lightx2v正式版参考模式｜minimax_h3视频生视频图生视频工作流_2088211325951504385.json, 视频生成/图生视频/提速不减质｜MiniMax H3图生视频加速通道_2096569545073971201.json, 视频生成/文生视频/LightX2V Turbo加速｜MiniMax H3文生图生视频生视频工作流_2087187099337445378.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_94

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3首尾帧生视频｜官方加速版工作流制作_2096332861723996162.json、视频生成/图生视频/MiniMax-H3-多图参考视频生成（Lightx2v加速）_2086208730663841794.json、视频生成/图生视频/MiniMaxH3首尾帧图生视频模板｜图生视频快速生成_2090429460284796930.json、视频生成/图生视频/Minimax H3图生视频Lightx2v正式版生成工作流_2088211425947897858.json、视频生成/图生视频/Minimax H3首尾帧生视频In8加速版图生视频生成_2088209952254021634.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 10/11 个有
- `MiniMaxH3ImageToVideo` —— 7/11 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/11 个有
- `ImageResizeKJv2` —— 4/11 个有
- `MiniMaxH3ReferenceToVideo` —— 4/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `Seed (rgthree)` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `INTConstant` —— 1/11 个有
- `QwenTE_ImageInfer` —— 1/11 个有
- `QwenTE_ModelLoader` —— 1/11 个有
- `RHHiddenNodes` —— 1/11 个有
- `RH_LLMAPI_NODE` —— 1/11 个有
- `TE_H3_Prompt_Enhancer` —— 1/11 个有
- `TE_prompt_text` —— 1/11 个有
- `TE_text_display` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `easy showAnything` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
