---
name: unknown_workflow_video_clip_unet_7
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9382
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, LoadImage, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1图生视频_1924384393446477826.json, 视频生成/图生视频/Wan2.1图生视频_1940719231082328066.json, 视频生成/图生视频/Wan2.1图生视频_1985686489952657410.json, 视频生成/图生视频/Wan2.1图生视频_2008112193308467202.json, 视频生成/图生视频/Wan2.1图生视频工作流（ComfyUI官方版）_1935896617889558530.json, 视频生成/图生视频/Wan2.1首尾帧动画_1925841932033937410.json, 视频生成/图生视频/Wan2.1首尾帧工作流（ComfyUI官方版）_1935900536141246465.json, 视频生成/图生视频/wan2.2-i2v_官方版图生视频_1967246222643826690.json, 视频生成/图生视频/wan2.2图生视频_2032294659132755970.json, 视频生成/图生视频/wan2.2图生视频首尾帧_2040056903719460866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Wan2.1图生视频_1924384393446477826.json、视频生成/图生视频/Wan2.1图生视频_1940719231082328066.json、视频生成/图生视频/Wan2.1图生视频_1985686489952657410.json、视频生成/图生视频/Wan2.1图生视频_2008112193308467202.json、视频生成/图生视频/Wan2.1图生视频工作流（ComfyUI官方版）_1935896617889558530.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `LoadImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 7/10 个有
- `WanImageToVideo` —— 7/10 个有
- `ModelSamplingSD3` —— 5/10 个有
- `ImageResize+` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `KSamplerAdvanced` —— 3/10 个有
- `LoraLoaderModelOnly` —— 3/10 个有
- `WanFirstLastFrameToVideo` —— 3/10 个有
- `ImageResizeKJ` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `Label (rgthree)` —— 2/10 个有
- `GetImageSize+` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 7 | 80% |
| Prompt 约束强度(CFG) | 6 | 3 - 8 | 10 | 69% |
| 采样算法 | uni_pc | - | 10 | 50% |
| 调度器 | simple | - | 10 | 70% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，7 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 3 - 8，10 个样本
- 采样算法 最常用 uni_pc，10 个样本，一致性 50%
- 调度器 最常用 simple，10 个样本，一致性 70%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
