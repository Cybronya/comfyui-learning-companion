---
name: unknown_workflow_video_sampler_vae_16
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.900667
common_nodes: [ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTeaCache, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Phantom多图参考_1915754654502682625.json, 图片生成/图生图/多图结合)_1916087298910523393.json, 平台全量/Phantom多图参考生成视频一致性_1928013554689916930.json, 视频生成/图生视频/2025-05-30 phantom_14B 主体一致性_1927564168260653058.json, 视频生成/图生视频/B4-Wan2.1多图融合视频phantom FusionX+NAG_1934069009803300865.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_1934659056122404865.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2074784823415238657.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2075377301298176002.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2077272902344470529.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2077571245901705218.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2077595441516081153.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2078326809900445698.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2080492754869772289.json, 视频生成/图生视频/LORA版本-电商带货FusionX-Phantom_2090234340373516290.json, 视频生成/图生视频/phantom多图参考_1916775902779211777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_16

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Phantom多图参考_1915754654502682625.json、图片生成/图生图/多图结合)_1916087298910523393.json、平台全量/Phantom多图参考生成视频一致性_1928013554689916930.json、视频生成/图生视频/2025-05-30 phantom_14B 主体一致性_1927564168260653058.json、视频生成/图生视频/B4-Wan2.1多图融合视频phantom FusionX+NAG_1934069009803300865.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoModelLoader`
- `WanVideoPhantomEmbeds`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 14/15 个有
- `WanVideoTextEncode` —— 14/15 个有
- `WanVideoTorchCompileSettings` —— 14/15 个有
- `ImageConcatMulti` —— 13/15 个有
- `CLIPLoader` —— 11/15 个有
- `CLIPTextEncode` —— 11/15 个有
- `WanVideoTextEmbedBridge` —— 11/15 个有
- `ColorMatch` —— 9/15 个有
- `Primitive integer [Crystools]` —— 9/15 个有
- `Text Multiline` —— 9/15 个有
- `WanVideoLoraSelect` —— 9/15 个有
- `INTConstant` —— 5/15 个有
- `WanVideoVRAMManagement` —— 4/15 个有
- `easy imageRemBg` —— 2/15 个有
- `Bjornulf_ShowStringText` —— 1/15 个有
- `Joy_caption_two` —— 1/15 个有
- `Joy_caption_two_load` —— 1/15 个有
- `WanVideoApplyNAG` —— 1/15 个有
- `WanVideoExperimentalArgs` —— 1/15 个有
- `WanVideoTextEncodeSingle` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
