---
title: "Social Media Integrations"
created: "2026-04-08"
updated: "2026-04-21"
type: "concept"
---

# Social Media Integrations

## Platforms Configured

### 📱 Telegram
- **Primary channel** for Hermes communication
- **User ID:** `1808182714`
- **dmPolicy:** allowlist
- **Status:** Connected via gateway

### 📸 Instagram (via Brisa Social)
- **Important rule:** Never post without images
- **Requirement:** Instagram requires images for all posts
- **Consistency:** Maintain image consistency across all platforms
- **Integration:** Managed through Brisa Social platform

### 🐦 X/Twitter (via xitter skill)
- **CLI client:** x-cli terminal client
- **Skill:** `xitter` for interaction
- **Capabilities:** Posting, reading, monitoring

### 📊 Buffer (via Hermes imports)
- **Skill:** `buffer-rate-limit-monitor`
- **Purpose:** Rate limit monitoring for Buffer GraphQL API
- **Integration:** Migrated from previous workspace

## Posting Guidelines

### General Rules
1. **Always include images** for Instagram posts
2. **Maintain consistency** across platforms
3. **Schedule posts** for optimal timing
4. **Monitor engagement** and adjust strategy
5. **Follow platform-specific** best practices

### Content Strategy
- **Personal updates:** Family, dogs, daily life
- **Technical content:** Hermes, automation, AI
- **Project updates:** Development progress
- **Educational content:** Tips and tutorials
- **Community engagement:** Responses and interactions

### Automation Rules
- **Hermes can post** on behalf of Jorge
- **Manual review** recommended for important posts
- **Scheduled posts** can be automated
- **Emergency stop** capability available

## Skills Integration

### Available Skills
- **xitter:** X/Twitter interaction via CLI
- **buffer-rate-limit-monitor:** Buffer API monitoring
- **Brisa Social Posts:** Platform-specific posting rules

### Skill Dependencies
- **Telegram integration:** Required for notifications
- **Image handling:** Required for Instagram
- **API keys:** Required for platform access
- **Rate limiting:** Managed by monitoring skills

## Configuration

### Telegram
```yaml
telegram:
  user_id: "1808182714"
  dmPolicy: "allowlist"
  gateway: "connected"
```

### Instagram (via Brisa Social)
```yaml
brisa_social:
  platforms:
    instagram:
      require_images: true
      consistency: "cross-platform"
      automation: "semi-automated"
```

### X/Twitter
```yaml
twitter:
  client: "x-cli"
  skill: "xitter"
  capabilities: ["post", "read", "monitor"]
```

## Monitoring and Analytics

### Metrics Tracked
- **Engagement rates** per platform
- **Post frequency** and timing
- **Audience growth** over time
- **Content performance** by type

### Alerting
- **Rate limit warnings** from Buffer
- **Post failure notifications**
- **Engagement threshold alerts**
- **Platform API status**

## Best Practices

### Content Creation
1. **Plan ahead** with content calendar
2. **Create platform-specific** variations
3. **Include relevant hashtags**
4. **Engage with comments** and messages
5. **Analyze performance** regularly

### Technical Management
1. **Keep API keys secure**
2. **Monitor rate limits**
3. **Update integration skills** regularly
4. **Test posting workflow** before automation
5. **Maintain backup** of important content

### Privacy and Security
1. **Review posts** before automated publishing
2. **Limit personal information** exposure
3. **Use allowlists** for direct messages
4. **Monitor for unauthorized access**
5. **Regular security audits** of integrations

---

*Última actualización: 08/04/2026*