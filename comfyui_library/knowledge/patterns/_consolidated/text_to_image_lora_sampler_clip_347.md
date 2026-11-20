---
name: text_to_image_lora_sampler_clip_347
type: Text To Image
frequency: 6
level: strong
coverage: 0.843667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, PreviewAny, UNETLoader, VAEDecode, VAELoader, easy saveText, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多模态提示词重写专用｜H3工作流一键优化生成_2094725404073480193.json, 图片生成/文生图/gemini3.6文生图AI绘画生成工作流_2088403565512585218.json, 图片生成/文生图/gemini3.6视频6图双文本生成｜多模态文生图工作流_2096731827070390274.json, 图片生成/文生图/小空间可加视频｜gemini3.6文生图轻量玩法_2089033642176770049.json, 图片生成/文生图/文生图图片生成｜gemini3.6工作流_2088382298440953858.json, 视频生成/文生视频/全自动提示词重写导演台｜H3三模视频一键生成_2094722482027720706.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_347

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/多模态提示词重写专用｜H3工作流一键优化生成_2094725404073480193.json、图片生成/文生图/gemini3.6文生图AI绘画生成工作流_2088403565512585218.json、图片生成/文生图/gemini3.6视频6图双文本生成｜多模态文生图工作流_2096731827070390274.json、图片生成/文生图/小空间可加视频｜gemini3.6文生图轻量玩法_2089033642176770049.json、图片生成/文生图/文生图图片生成｜gemini3.6工作流_2088382298440953858.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewAny`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy saveText`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `RHLLMChatNode` —— 4/6 个有
- `GetVideoComponents` —— 2/6 个有
- `LlamaServeDocH3OmniGenerate` —— 2/6 个有
- `LlamaServeDocLoader` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `ComfyMiniMaxH3Director` —— 1/6 个有
- `CreateVideo` —— 1/6 个有
- `LoraLoaderBypassModelOnly` —— 1/6 个有
- `MiniMaxH3DirectorRefine` —— 1/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `SaveVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
