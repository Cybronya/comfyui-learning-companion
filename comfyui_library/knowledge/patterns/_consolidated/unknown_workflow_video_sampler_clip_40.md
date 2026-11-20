---
name: unknown_workflow_video_sampler_clip_40
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.949615
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/产品图片_360度旋转工作流_2016158718987079682.json, 视频生成/图生视频/人物生气特效｜Wan2.1_1938851754044018689.json, 视频生成/图生视频/压扁万物=艾橘溪_1899415401065828354.json, 视频生成/图生视频/变胖飞走+通义万相=艾橘溪_1900846163619389442.json, 视频生成/图生视频/地标建筑飞天特效_1900090091270987777.json, 视频生成/图生视频/捏捏乐+通义万相=艾橘溪_1900825368478261250.json, 视频生成/图生视频/捏捏乐，WAN2.1万相LORA工作流_1899052254505385985.json, 视频生成/图生视频/捏爆特效 捏扁特效---通义万相wan2.1 图生视频新玩儿法_1899003016236941314.json, 视频生成/图生视频/最强视频开源模型-Wan2.1-360旋转_1900079206938587137.json, 视频生成/图生视频/电商产品360展示    UP楚门的AI世界_1899792108687863809.json, 视频生成/图生视频/通义万相wan2.1 图生视频 720P高清版_1894738389084602370.json, 视频生成/图生视频/通义万相之图片捏捏乐_1940715917842214913.json, 视频生成/图生视频/🦖wan2.1 变玩偶捏捏_1925461590995292161.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_40

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/产品图片_360度旋转工作流_2016158718987079682.json、视频生成/图生视频/人物生气特效｜Wan2.1_1938851754044018689.json、视频生成/图生视频/压扁万物=艾橘溪_1899415401065828354.json、视频生成/图生视频/变胖飞走+通义万相=艾橘溪_1900846163619389442.json、视频生成/图生视频/地标建筑飞天特效_1900090091270987777.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 13 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadWanVideoT5TextEncoder` —— 12/13 个有
- `WanVideoLoraSelect` —— 12/13 个有
- `WanVideoTextEncode` —— 12/13 个有
- `LayerUtility: PurgeVRAM` —— 5/13 个有
- `Int` —— 4/13 个有
- `TextInput_` —— 3/13 个有
- `WanVideoTorchCompileSettings` —— 3/13 个有
- `GetImageRangeFromBatch` —— 1/13 个有
- `Image Batch` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有
- `RH_Captioner` —— 1/13 个有
- `WanVideoSetBlockSwap` —— 1/13 个有
- `WanVideoTextEncodeCached` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
