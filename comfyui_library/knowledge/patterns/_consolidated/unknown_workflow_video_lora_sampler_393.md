---
name: unknown_workflow_video_lora_sampler_393
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.983
common_nodes: [INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: [String Literal]
members: [视频生成/文生视频/1963899111291572225.json, 视频生成/文生视频/1963907661271224322.json, 视频生成/文生视频/1963909620598394882.json, 视频生成/文生视频/WAN2.2-AllInOne控制+参考_2072999603861233664.json, 视频生成/文生视频/WAN2.2-AllInOne文生视频_2072999602099625984.json, 视频生成/文生视频/WAN2.2-AllInOne首尾帧_2072999603420831744.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_393

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/1963899111291572225.json、视频生成/文生视频/1963907661271224322.json、视频生成/文生视频/1963909620598394882.json、视频生成/文生视频/WAN2.2-AllInOne控制+参考_2072999603861233664.json、视频生成/文生视频/WAN2.2-AllInOne文生视频_2072999602099625984.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 4/6 个有
- `ImageResizeKJv2` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `String Literal` —— 4/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `WanVideoVACEStartToEndFrame` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：String Literal
