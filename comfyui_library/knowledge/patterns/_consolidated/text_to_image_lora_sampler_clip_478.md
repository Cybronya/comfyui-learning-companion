---
name: text_to_image_lora_sampler_clip_478
type: Text To Image
frequency: 4
level: strong
coverage: 0.88225
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image-LORA  光影实验 01_2001814077842288642.json, 图片生成/文生图/Z-image-LORA  光影实验（柔光） 02_2002288520590966786.json, 图片生成/文生图/Z-image文生图（反推）_2041148950798929921.json, 图片生成/文生图/【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_478

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image-LORA  光影实验 01_2001814077842288642.json、图片生成/文生图/Z-image-LORA  光影实验（柔光） 02_2002288520590966786.json、图片生成/文生图/Z-image文生图（反推）_2041148950798929921.json、图片生成/文生图/【 自练LORA 】Z-image-Turbo-LoRa：超可爱！Q版动物油画头像！_2001585182400475138.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MultiTextConcatenate` —— 3/4 个有
- `MuyeTextEditOutput` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ShowAnything|Mie` —— 3/4 个有
- `RH_Captioner_Pro` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 768 - 1280 | 4 | 81% |
| 高度 | 1920 | 1280 - 1920 | 4 | 84% |
| 采样步数 | 10 | 10 - 12 | 4 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1280，观测区间 768 - 1280，4 个样本，取值集中（一致性 81%）
- 高度 中位数 1920，观测区间 1280 - 1920，4 个样本，取值集中（一致性 84%）
- 采样步数 中位数 10，观测区间 10 - 12，4 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
