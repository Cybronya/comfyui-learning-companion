---
name: text_to_image_lora_sampler_clip_262
type: Text To Image
frequency: 8
level: strong
coverage: 0.86425
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多模态提示词重写专用｜H3工作流一键优化生成_2094725404073480193.json, 图片生成/文生图/gemini3.6文生图AI绘画生成工作流_2088403565512585218.json, 图片生成/文生图/gemini3.6视频6图双文本生成｜多模态文生图工作流_2096731827070390274.json, 图片生成/文生图/小空间可加视频｜gemini3.6文生图轻量玩法_2089033642176770049.json, 图片生成/文生图/文生图图片生成｜gemini3.6工作流_2088382298440953858.json, 视频生成/文生视频/Seedance 2.0 Global Fast多模态全能参考视频｜4K文图视频参考_2097977539267489794.json, 视频生成/文生视频/Seedance 2.0 Global Mini多模态全能参考视频｜4K文图视频参考全支持_2097900436190752770.json, 视频生成/文生视频/全自动提示词重写导演台｜H3三模视频一键生成_2094722482027720706.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_262

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/多模态提示词重写专用｜H3工作流一键优化生成_2094725404073480193.json、图片生成/文生图/gemini3.6文生图AI绘画生成工作流_2088403565512585218.json、图片生成/文生图/gemini3.6视频6图双文本生成｜多模态文生图工作流_2096731827070390274.json、图片生成/文生图/小空间可加视频｜gemini3.6文生图轻量玩法_2089033642176770049.json、图片生成/文生图/文生图图片生成｜gemini3.6工作流_2088382298440953858.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：86%

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
- `LoadVideo` —— 6/8 个有
- `PreviewAny` —— 6/8 个有
- `easy saveText` —— 6/8 个有
- `LoadAudio` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `RHLLMChatNode` —— 4/8 个有
- `MuyeTextEditOutput` —— 3/8 个有
- `SaveVideo` —— 3/8 个有
- `GetVideoComponents` —— 2/8 个有
- `LlamaServeDocH3OmniGenerate` —— 2/8 个有
- `LlamaServeDocLoader` —— 2/8 个有
- `ComfyMiniMaxH3Director` —— 1/8 个有
- `CreateVideo` —— 1/8 个有
- `LoraLoaderBypassModelOnly` —— 1/8 个有
- `MiniMaxH3DirectorRefine` —— 1/8 个有
- `RH_BytedanceSeedance20GlobalFastMultimodalVideo` —— 1/8 个有
- `RH_BytedanceSeedance20GlobalMiniMultimodalVideo` —— 1/8 个有

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
