---
name: text_to_image_lora_sampler_clip_345
type: Text To Image
frequency: 6
level: strong
coverage: 0.904833
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, RHLLMChatNode, SaveImage, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Krea2 双图风格融合（创意洗图）_2078736945521455106.json, 图片生成/文生图/Krea2 文生图多风格优化+双图风格迁移智能优化版_2073044999301844994.json, 图片生成/文生图/Krea2 文生图多风格优化+双图风格迁移智能优化版_2078759570259927041.json, 图片生成/文生图/krea2 文生图多风格优化+双图风格智能迁移_2073314611042017281.json, 图片生成/文生图/krea2 文生图多风格优化+双图风格迁移智能优化版_2072983737209548802.json, 图片生成/文生图/krea2 文生图多风格优化+双图风格迁移智能优化版_2080467909574488065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_345

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Krea2 双图风格融合（创意洗图）_2078736945521455106.json、图片生成/文生图/Krea2 文生图多风格优化+双图风格迁移智能优化版_2073044999301844994.json、图片生成/文生图/Krea2 文生图多风格优化+双图风格迁移智能优化版_2078759570259927041.json、图片生成/文生图/krea2 文生图多风格优化+双图风格智能迁移_2073314611042017281.json、图片生成/文生图/krea2 文生图多风格优化+双图风格迁移智能优化版_2072983737209548802.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RHLLMChatNode`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `DapaoImageRatioLimitNode` —— 5/6 个有
- `easy anythingIndexSwitch` —— 5/6 个有
- `easy int` —— 5/6 个有
- `孤海注释` —— 3/6 个有
- `AspectRatio` —— 2/6 个有
- `SizeSelector` —— 2/6 个有
- `DF_Latent_Scale_to_side` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `TTResolutionSelector` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1024 | 1024 - 1024 | 6 | 100% |
| 采样步数 | 10 | 10 - 10 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 10 - 10，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
