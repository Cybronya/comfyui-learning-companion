---
name: unknown_workflow_sampler_clip_unet_310
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.92925
common_nodes: [CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, image_scale_pixel_v2]
problems: []
missing: []
members: [图片生成/文生图/Anima Preview3图生图_2042205599336763393.json, 图片生成/文生图/Anima Preview3局部重绘_2042205589152997377.json, 图片生成/文生图/Anima-Base局部重绘_2055109942587215873.json, 图片生成/文生图/WAI-ANIMA图生图_2046194201804677121.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_310

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Anima Preview3图生图_2042205599336763393.json、图片生成/文生图/Anima Preview3局部重绘_2042205589152997377.json、图片生成/文生图/Anima-Base局部重绘_2055109942587215873.json、图片生成/文生图/WAI-ANIMA图生图_2046194201804677121.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `image_scale_pixel_v2`

**可变部分**（部分 workflow 才有）：
- `DifferentialDiffusion` —— 2/4 个有
- `Float` —— 2/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `SetLatentNoiseMask` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | beta57 | - | 4 | 100% |
| Prompt 约束强度(CFG) | 30 | 30 - 30 | 4 | 100% |
| 采样算法 | -1 | -1 - -1 | 4 | 100% |
| 调度器 | 0.865 | 0.5 - 1 | 4 | 74% |
| 重绘幅度 | 3 | 3 - 3 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 beta57，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 -1，观测区间 -1 - -1，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 0.865，观测区间 0.5 - 1，4 个样本
- 重绘幅度 中位数 3，观测区间 3 - 3，4 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 3，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
