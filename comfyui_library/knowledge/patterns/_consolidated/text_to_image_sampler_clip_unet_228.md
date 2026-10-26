---
name: text_to_image_sampler_clip_unet_228
type: Text To Image
frequency: 2
level: weak
coverage: 0.882
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, RH_LLMAPI_NODE, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/QWEN-IMAGE 海报生成_1957100875913289730.json, 图片生成/文生图/QWEN文生图【LLM辅助】_1952896951139430401.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_228

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/QWEN-IMAGE 海报生成_1957100875913289730.json、图片生成/文生图/QWEN文生图【LLM辅助】_1952896951139430401.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `StringReplace` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 70% |
| 高度 | 1304 | - | 2 | 98% |
| 采样步数 | 15 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 2.5 | - | 2 | 40% |
| 采样算法 | res_multistep | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本
- 高度 中位数 1304，样本不足，未给区间，2 个样本，取值集中（一致性 98%）
- 采样步数 中位数 15，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 2.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 res_multistep，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
