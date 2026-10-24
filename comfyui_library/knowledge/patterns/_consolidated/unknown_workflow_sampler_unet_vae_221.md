---
name: unknown_workflow_sampler_unet_vae_221
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.988
common_nodes: [BasicScheduler, CLIPLoader, EmptyLatentImage, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Boogu+vr2.5_光学眼镜场景 opticscene_2100503999580565506.json, 图片生成/图生图/boogu编辑图像_2069048520065245185.json, 图片生成/文生图/Boogu_Base_edit_图像编辑工作流_2069278108913594370.json, 图片生成/文生图/boogu_edit_example_2068254277000327170.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_221

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Boogu+vr2.5_光学眼镜场景 opticscene_2100503999580565506.json、图片生成/图生图/boogu编辑图像_2069048520065245185.json、图片生成/文生图/Boogu_Base_edit_图像编辑工作流_2069278108913594370.json、图片生成/文生图/boogu_edit_example_2068254277000327170.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/4 个有
- `DF_Get_image_size` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `SeedVR2LoadDiTModel` —— 1/4 个有
- `SeedVR2LoadVAEModel` —— 1/4 个有
- `SeedVR2VideoUpscaler` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1080 | 4 | 98% |
| 高度 | 1024 | 1024 - 1920 | 4 | 69% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1080，4 个样本，取值集中（一致性 98%）
- 高度 中位数 1024，观测区间 1024 - 1920，4 个样本
