---
name: text_to_image_lora_sampler_clip_306
type: Text To Image
frequency: 3
level: strong
coverage: 0.843
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, MultiTextConcatenate, MuyeTextEditOutput, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-LORA  光影实验 01_2001814077842288642.json, 图片生成/文生图/Z-image-LORA  光影实验（柔光） 02_2002288520590966786.json, 图片生成/文生图/【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_306

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-LORA  光影实验 01_2001814077842288642.json、图片生成/文生图/Z-image-LORA  光影实验（柔光） 02_2002288520590966786.json、图片生成/文生图/【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MultiTextConcatenate`
- `MuyeTextEditOutput`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner_Pro` —— 2/3 个有
- `ShowAnything|Mie` —— 2/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
