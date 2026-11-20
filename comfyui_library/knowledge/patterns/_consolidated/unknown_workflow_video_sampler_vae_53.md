---
name: unknown_workflow_video_sampler_vae_53
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9355
common_nodes: [ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoModelLoader, WanVideoPhantomEmbeds, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/skyreelsv3+主体一致性 (1)_2019437337008148481.json, 视频生成/图生视频/万相Phantom14B图片编辑工作流_1927590039822438402.json, 视频生成/图生视频/上传一张图生成电商产品展示视频（phantom主体一致性）_1917815570186567682.json, 视频生成/图生视频/多图参考视频媲美可灵1.6_1925799442136666113.json, 视频生成/图生视频/字节Phantom 14B_1927551955353374722.json, 视频生成/图生视频/字节Phantom14B_最新多图参考一致性视频(电商带货)_1916395426835005442.json, 视频生成/图生视频/字节Phantom14B_最新多图参考一致性视频_1927541511028903938.json, 视频生成/图生视频/字节Phantom14B图生视频_1927944176032464897.json, 视频生成/图生视频/字节Phantom14B最新主体一致性(电商广告视频生成)_1915051981709242369.json, 视频生成/图生视频/电商带货FusionX-Phantom加速版14B_2108761890527735810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_53

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/skyreelsv3+主体一致性 (1)_2019437337008148481.json、视频生成/图生视频/万相Phantom14B图片编辑工作流_1927590039822438402.json、视频生成/图生视频/上传一张图生成电商产品展示视频（phantom主体一致性）_1917815570186567682.json、视频生成/图生视频/多图参考视频媲美可灵1.6_1925799442136666113.json、视频生成/图生视频/字节Phantom 14B_1927551955353374722.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
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
- `WanVideoTorchCompileSettings` —— 9/10 个有
- `WanVideoTeaCache` —— 8/10 个有
- `Primitive integer [Crystools]` —— 7/10 个有
- `ImageConcatMulti` —— 5/10 个有
- `PreviewImage` —— 5/10 个有
- `Text Multiline` —— 5/10 个有
- `INTConstant` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `WanVideoVRAMManagement` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
