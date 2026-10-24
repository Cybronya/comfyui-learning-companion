---
name: unknown_workflow_video_sampler_vae_114
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9696
common_nodes: [ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1-FusionX-Phantom图生视频_1933830399460335618.json, 视频生成/图生视频/Wan2.1-FusionX-Phantom图生视频电商工作流_1934541885903937537.json, 视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商产品展示视频_1937023070462726146.json, 视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商版_1935608698565742593.json, 视频生成/图生视频/多图合成视频工作流_2019122277626941442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_114

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.1-FusionX-Phantom图生视频_1933830399460335618.json、视频生成/图生视频/Wan2.1-FusionX-Phantom图生视频电商工作流_1934541885903937537.json、视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商产品展示视频_1937023070462726146.json、视频生成/图生视频/Wan2.1-Phantom+FusionX-LORA电商版_1935608698565742593.json、视频生成/图生视频/多图合成视频工作流_2019122277626941442.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Text Multiline` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `WanVideoLoraSelect` —— 3/5 个有
- `DF_Integer` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `JWInteger` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoSetBlockSwap` —— 1/5 个有
- `WanVideoSetLoRAs` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
