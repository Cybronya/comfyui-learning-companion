---
name: unknown_workflow_upscale_clip_unet_6
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9845
common_nodes: [CLIPTextEncode, LoadImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/高清放大保留细节_1922117384772190210.json, 平台全量/Z-Image-Turbo-SD放大_1994037869108985857.json, 平台全量/sd图像4k放大_1995752554317361154.json, 平台全量/自己用：FLUX模糊变清晰_1940648776237477890.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_clip_unet_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/高清放大保留细节_1922117384772190210.json、平台全量/Z-Image-Turbo-SD放大_1994037869108985857.json、平台全量/sd图像4k放大_1995752554317361154.json、平台全量/自己用：FLUX模糊变清晰_1940648776237477890.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `Florence2ModelLoader` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `CLIPLoader` —— 1/4 个有
- `DifferentialDiffusion` —— 1/4 个有
- `Float` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `ImageSharpen` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
