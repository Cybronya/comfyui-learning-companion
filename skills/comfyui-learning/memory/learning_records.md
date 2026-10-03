# 学习记录（learning_records）

> 流水账：每学会一个新东西（节点 / 模型 / 原理 / 踩坑），追加一条。
> 新知识本体写到 `knowledge/` 对应目录，这里只留索引与心得。

## 记录格式

```
### YYYY-MM-DD｜主题（一句话）
- 类型：节点 / 模型 / 原理 / 踩坑
- 新增卡片：knowledge/xxx/yyy.md（或"无，仅备忘"）
- 要点：
  - …
- 来源：工作流分析 / 上游 README / 官方文档 / 实测
```

---

### 2026-10-04｜知识库初始化
- 类型：节点 / 模型 / 原理（建库）
- 新增卡片：
  - knowledge/nodes/sampler.md（KSampler 家族）
  - knowledge/nodes/vae.md（VAE 编解码与 tiled）
  - knowledge/nodes/controlnet.md（ControlNet 应用）
  - knowledge/models/sd.md（SD1.5/SDXL/SD3）
  - knowledge/models/flux.md（FLUX.1 dev/schnell）
  - knowledge/models/wan.md（Wan2.1/2.2 视频链路，含两段采样与蒸馏 LoRA）
  - knowledge/concepts/latent.md（潜空间与视频 latent）
  - knowledge/concepts/diffusion.md（去噪 / CFG / scheduler / flow matching）
- 要点：
  - 本项目主场景是视频生成（MiniMax H3），Wan 卡片留了 TODO：H3 专属节点与 Wan 链路的差异对照，待首个 H3 工作流分析后补齐。
  - 节点插件归属一律对照 comfyui/custom_nodes/NODES_SOURCES.md。
- 来源：ComfyUI 内置节点文档 / BFL & Wan 官方说明 / 社区通行实践
