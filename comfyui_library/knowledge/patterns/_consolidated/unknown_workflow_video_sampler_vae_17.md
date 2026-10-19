---
name: unknown_workflow_video_sampler_vae_17
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.9282
common_nodes: [ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2019437337008148481.json, 视频生成/图生视频/1927590039822438402.json, 视频生成/图生视频/1917815570186567682.json, 视频生成/图生视频/1925799442136666113.json, 视频生成/图生视频/1927551955353374722.json, 视频生成/图生视频/1916395426835005442.json, 视频生成/图生视频/1927541511028903938.json, 视频生成/图生视频/1927944176032464897.json, 视频生成/图生视频/1915051981709242369.json, 视频生成/图生视频/2039636071985713154.json, 视频生成/图生视频/2064931253647929346.json, 视频生成/图生视频/1934089550950260738.json, 视频生成/图生视频/电商带货FusionX-Phantom加速版14B_2108761890527735810.json, 视频生成/图生视频/1934241189509951489.json, 视频生成/文生视频/1935520036046176257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_17

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/2019437337008148481.json、视频生成/图生视频/1927590039822438402.json、视频生成/图生视频/1917815570186567682.json、视频生成/图生视频/1925799442136666113.json、视频生成/图生视频/1927551955353374722.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：93%

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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 14/15 个有
- `Primitive integer [Crystools]` —— 12/15 个有
- `ImageConcatMulti` —— 10/15 个有
- `PreviewImage` —— 10/15 个有
- `Text Multiline` —— 10/15 个有
- `WanVideoTeaCache` —— 8/15 个有
- `easy clearCacheAll` —— 5/15 个有
- `INTConstant` —— 3/15 个有
- `CR Prompt Text` —— 2/15 个有
- `SetNode` —— 2/15 个有
- `ImageResizeKJv2` —— 1/15 个有
- `RH_Translator` —— 1/15 个有
- `WanVideoVRAMManagement` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
