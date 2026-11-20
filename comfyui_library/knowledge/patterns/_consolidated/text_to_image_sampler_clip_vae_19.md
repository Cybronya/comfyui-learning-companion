---
name: text_to_image_sampler_clip_vae_19
type: Text To Image
frequency: 6
level: moderate
coverage: 0.871167
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/三图融合Qwen Edit 2509 nunchaku加速_1963483303460442113.json, 图片生成/图生图/产品可视化-任意角度可编辑-multiangle_2009653208204972034.json, 图片生成/图生图/人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090.json, 图片生成/图生图/人物面部+全身三视图-高清直出_2072004887482814465.json, 图片生成/图生图/即梦、小云雀、豆包、超能视频2.0真人过审核方法-FireRed-Image-Edit 1.1_2036801337580589057.json, 图片生成/文生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2083015619733180417.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_19

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/三图融合Qwen Edit 2509 nunchaku加速_1963483303460442113.json、图片生成/图生图/产品可视化-任意角度可编辑-multiangle_2009653208204972034.json、图片生成/图生图/人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090.json、图片生成/图生图/人物面部+全身三视图-高清直出_2072004887482814465.json、图片生成/图生图/即梦、小云雀、豆包、超能视频2.0真人过审核方法-FireRed-Image-Edit 1.1_2036801337580589057.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/6 个有
- `UNETLoader` —— 5/6 个有
- `JjkText` —— 4/6 个有
- `SeedVR2` —— 4/6 个有
- `CustomAddLabel` —— 3/6 个有
- `RunningHub Deepcleaner` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `Int` —— 1/6 个有
- `NunchakuQwenImageDiTLoader` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `PrimitiveString` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 2 | 6 | 68% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1052 | 720 - 1920 | 6 | 59% |
| 高度 | 1280 | 1080 - 1920 | 6 | 79% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 720 - 1920，6 个样本
- 高度 中位数 1280，观测区间 1080 - 1920，6 个样本
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
