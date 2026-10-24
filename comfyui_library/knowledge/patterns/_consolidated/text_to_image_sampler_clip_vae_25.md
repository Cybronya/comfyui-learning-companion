---
name: text_to_image_sampler_clip_vae_25
type: Text To Image
frequency: 6
level: moderate
coverage: 0.8575
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen_multiple2511 图片多角度、多视角编辑工作流_2046132302052331522.json, 图片生成/图生图/三图融合Qwen Edit 2509 nunchaku加速_1963483303460442113.json, 图片生成/图生图/任意角度分镜制作-qwen edit 2511_2010346866856173570.json, 图片生成/图生图/单图编辑Qwen Edit 2509 nunchaku_1963473556313182209.json, 图片生成/图生图/可视化角度控制改图Qwen Multiangle Camera_2014245627441451009.json, 图片生成/图生图/效果图人物改变相机角度，直接拖动改为位置即可_2015794374164094978.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_25

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/qwen_multiple2511 图片多角度、多视角编辑工作流_2046132302052331522.json、图片生成/图生图/三图融合Qwen Edit 2509 nunchaku加速_1963483303460442113.json、图片生成/图生图/任意角度分镜制作-qwen edit 2511_2010346866856173570.json、图片生成/图生图/单图编辑Qwen Edit 2509 nunchaku_1963473556313182209.json、图片生成/图生图/可视化角度控制改图Qwen Multiangle Camera_2014245627441451009.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

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
- `LoraLoaderModelOnly` —— 4/6 个有
- `QwenMultiangleCameraNode` —— 4/6 个有
- `easy imageSize` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `UNETLoader` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `NunchakuQwenImageDiTLoader` —— 2/6 个有
- `PrimitiveString` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1024 - 1280 | 6 | 90% |
| 高度 | 720 | 720 - 1536 | 6 | 61% |
| 采样步数 | 8 | 8 - 20 | 6 | 53% |
| Prompt 约束强度(CFG) | 2 | 1 - 2 | 6 | 72% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1024 - 1280，6 个样本，取值集中（一致性 90%）
- 高度 中位数 720，观测区间 720 - 1536，6 个样本
- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 2，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
