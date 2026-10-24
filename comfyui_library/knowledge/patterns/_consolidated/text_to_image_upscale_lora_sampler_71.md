---
name: text_to_image_upscale_lora_sampler_71
type: Text To Image
frequency: 4
level: moderate
coverage: 0.8955
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2-turbo-文生图_2070088731339612162.json, 图片生成/文生图/Krea2-turbo-文生图_2073296094896939010.json, 图片生成/文生图/anima文生图_2080943871458107394.json, 图片生成/文生图/anima文生图_2081302154224168962.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_71

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea2-turbo-文生图_2070088731339612162.json、图片生成/文生图/Krea2-turbo-文生图_2073296094896939010.json、图片生成/文生图/anima文生图_2080943871458107394.json、图片生成/文生图/anima文生图_2081302154224168962.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 2/4 个有
- `KOOK_ImageCompression` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `TextBoxMira` —— 2/4 个有
- `YC_ShowText` —— 2/4 个有
- `easy promptConcat` —— 2/4 个有
- `easy promptLine` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1112 | 1024 - 1200 | 4 | 92% |
| 高度 | 1728 | 1536 - 1920 | 4 | 89% |
| 采样步数 | 19 | 8 - 30 | 4 | 42% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 40% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1112，观测区间 1024 - 1200，4 个样本，取值集中（一致性 92%）
- 高度 中位数 1728，观测区间 1536 - 1920，4 个样本，取值集中（一致性 89%）
- 采样步数 中位数 19，观测区间 8 - 30，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
