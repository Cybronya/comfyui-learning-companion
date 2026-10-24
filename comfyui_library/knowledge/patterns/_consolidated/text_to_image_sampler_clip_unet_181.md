---
name: text_to_image_sampler_clip_unet_181
type: Text To Image
frequency: 3
level: moderate
coverage: 0.888
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/QWEN-IMAGE 海报生成_1957100875913289730.json, 图片生成/文生图/QWEN文生图【LLM辅助】_1952896951139430401.json, 图片生成/文生图/xingtong_base_2037099688356220930.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_181

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/QWEN-IMAGE 海报生成_1957100875913289730.json、图片生成/文生图/QWEN文生图【LLM辅助】_1952896951139430401.json、图片生成/文生图/xingtong_base_2037099688356220930.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CR SDXL Aspect Ratio` —— 1/3 个有
- `ClipLoaderGGUF` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `StringReplace` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 720 - 1328 | 3 | 76% |
| 高度 | 1328 | 1280 - 1920 | 3 | 81% |
| 采样步数 | 20 | 10 - 50 | 3 | 36% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1080，观测区间 720 - 1328，3 个样本
- 高度 中位数 1328，观测区间 1280 - 1920，3 个样本，取值集中（一致性 81%）
- 采样步数 中位数 20，观测区间 10 - 50，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
