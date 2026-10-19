---
name: unknown_workflow_video_sampler_vae_19
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.896231
common_nodes: [ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTeaCache, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1927564168260653058.json, 视频生成/图生视频/1934069009803300865.json, 视频生成/图生视频/1934659056122404865.json, 视频生成/图生视频/2074784823415238657.json, 视频生成/图生视频/2075377301298176002.json, 视频生成/图生视频/2077272902344470529.json, 视频生成/图生视频/2077571245901705218.json, 视频生成/图生视频/2077595441516081153.json, 视频生成/图生视频/2078326809900445698.json, 视频生成/图生视频/2080492754869772289.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2090234340373516290.json, 视频生成/图生视频/1927371436502192130.json, 视频生成/图生视频/1916775902779211777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_19

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1927564168260653058.json、视频生成/图生视频/1934069009803300865.json、视频生成/图生视频/1934659056122404865.json、视频生成/图生视频/2074784823415238657.json、视频生成/图生视频/2075377301298176002.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 12/13 个有
- `WanVideoTextEncode` —— 12/13 个有
- `CLIPLoader` —— 11/13 个有
- `CLIPTextEncode` —— 11/13 个有
- `WanVideoTextEmbedBridge` —— 11/13 个有
- `ColorMatch` —— 9/13 个有
- `Primitive integer [Crystools]` —— 9/13 个有
- `Text Multiline` —— 9/13 个有
- `WanVideoLoraSelect` —— 9/13 个有
- `INTConstant` —— 4/13 个有
- `WanVideoVRAMManagement` —— 2/13 个有
- `easy imageRemBg` —— 2/13 个有
- `WanVideoApplyNAG` —— 1/13 个有
- `WanVideoExperimentalArgs` —— 1/13 个有
- `WanVideoTextEncodeSingle` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
